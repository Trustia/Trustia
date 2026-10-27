"""
TRUSTIA Otonom Sürüş Çekirdeği — ODD, ISO 21448 (SOTIF) ve UN/ECE R157 DSSAD Kara Kutu Modülü.

Bu modül, 1 Aralık 2024 tarihli ve 32739 sayılı Resmî Gazete'de yayımlanan
"Tam Otonom Araçların Otonom Sürüş Sistemine İlişkin Motorlu Araçların Tip Onayı
Hakkında Yönetmelik ((AB) 2022/1426)", ISO 26262 ASIL-D, ISO 21448 (SOTIF) ve
Birleşmiş Milletler UN/ECE R157 regülasyonlarının zorunlu kıldığı 4 temel
emniyet bileşenini içerir:

  1. OddDomainMonitor (Operasyonel Tasarım Alanı & Coğrafi Çit Denetleyicisi)
  2. Iso21448SotifSupervisor (Algı Belirsizliği, Sensör Körlüğü & Çapraz Doğrulama)
  3. UnR157DssadBlackbox (Kriptografik SHA-256 Zincirli Adli Bilişim Kara Kutusu)
  4. SimulationVsFieldProfile (Simülasyon İdeal Değerleri vs. Gerçek Saha Tolerans Modeli)
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# ============================================================================
# 1. ODD (OPERASYONEL TASARIM ALANI) VE COĞRAFİ ÇİT (GEOFENCE) DENETLEYİCİSİ
# ============================================================================

@dataclass
class OddBoundaryConfig:
    """Seviye-4 Robotaksi Operasyonel Tasarım Alanı (ODD) Sınır Parametreleri."""
    geofence_polygon_xy: List[Tuple[float, float]] = field(
        default_factory=lambda: [
            (-5000.0, -5000.0),
            (5000.0, -5000.0),
            (5000.0, 5000.0),
            (-5000.0, 5000.0),
        ]
    )
    max_speed_kmh: float = 50.0
    max_rainfall_mm_per_hr: float = 35.0
    min_visibility_m: float = 40.0
    max_road_slope_pct: float = 15.0
    require_lidar_healthy: bool = True


@dataclass
class OddEvaluationResult:
    """Anlık ODD uygunluk değerlendirme çıktısı."""
    within_odd: bool
    inside_geofence: bool
    speed_compliant: bool
    weather_compliant: bool
    slope_compliant: bool
    recommended_action: str          # "NOMINAL_CONTINUE", "DEGRADED_SLOWDOWN", "MRM_SAFE_PULLOVER"
    target_decel_mps2: float         # İhlal durumunda -1.5 m/s² kontrollü yavaşlama
    violation_reasons: List[str] = field(default_factory=list)


class OddDomainMonitor:
    """
    1 Aralık 2024 Resmî Gazete Yönetmeliği ((AB) 2022/1426) Uyumlu ODD Denetleyicisi.
    Aracın coğrafi sınır, hız, hava durumu ve eğim limitleri içinde kalmasını denetler.
    """

    def __init__(self, config: Optional[OddBoundaryConfig] = None) -> None:
        self.config = config or OddBoundaryConfig()

    def is_inside_geofence(self, x_m: float, y_m: float) -> bool:
        """Ray-Casting algoritması ile aracın izinli coğrafi poligon içinde olup olmadığını denetler."""
        poly = self.config.geofence_polygon_xy
        n = len(poly)
        if n < 3:
            return True

        inside = False
        j = n - 1
        for i in range(n):
            xi, yi = poly[i]
            xj, yj = poly[j]
            intersect = ((yi > y_m) != (yj > y_m)) and (
                x_m < (xj - xi) * (y_m - yi) / ((yj - yi) + 1e-12) + xi
            )
            if intersect:
                inside = not inside
            j = i
        return inside

    def evaluate(
        self,
        x_m: float,
        y_m: float,
        speed_kmh: float,
        rainfall_mm_hr: float = 0.0,
        visibility_m: float = 200.0,
        road_slope_pct: float = 0.0,
        lidar_healthy: bool = True,
    ) -> OddEvaluationResult:
        violations: List[str] = []

        in_geo = self.is_inside_geofence(x_m, y_m)
        if not in_geo:
            violations.append("GEOFENCE_BOUNDARY_EXCEEDED")

        speed_ok = speed_kmh <= (self.config.max_speed_kmh + 0.5)
        if not speed_ok:
            violations.append(f"SPEED_EXCEEDS_ODD_LIMIT_{speed_kmh:.1f}KMH")

        weather_ok = (
            rainfall_mm_hr <= self.config.max_rainfall_mm_per_hr
            and visibility_m >= self.config.min_visibility_m
        )
        if not weather_ok:
            violations.append("WEATHER_VISIBILITY_OUTSIDE_ODD")

        slope_ok = abs(road_slope_pct) <= self.config.max_road_slope_pct
        if not slope_ok:
            violations.append(f"ROAD_SLOPE_EXCEEDED_{road_slope_pct:.1f}PCT")

        if self.config.require_lidar_healthy and not lidar_healthy:
            violations.append("PRIMARY_3D_LIDAR_DEGRADED")

        within_odd = len(violations) == 0
        if within_odd:
            action = "NOMINAL_CONTINUE"
            decel = 0.0
        elif not in_geo or not lidar_healthy or not weather_ok:
            action = "MRM_SAFE_PULLOVER"
            decel = -1.5  # 1.5 m/s² kontrollü sağa çekme yavaşlaması
        else:
            action = "DEGRADED_SLOWDOWN"
            decel = -1.0

        return OddEvaluationResult(
            within_odd=within_odd,
            inside_geofence=in_geo,
            speed_compliant=speed_ok,
            weather_compliant=weather_ok,
            slope_compliant=slope_ok,
            recommended_action=action,
            target_decel_mps2=decel,
            violation_reasons=violations,
        )


# ============================================================================
# 2. ISO 21448 (SOTIF) — ALGI BELİRSİZLİĞİ VE SENSÖR KÖRLÜĞÜ DENETLEYİCİSİ
# ============================================================================

@dataclass
class SotifAssessment:
    """ISO 21448 SOTIF fonksiyonel yeterlilik değerlendirme sonucu."""
    sotif_safe: bool
    sensor_blindness_detected: bool
    cross_modal_agreement_score: float
    ai_uncertainty_entropy: float
    phantom_brake_prevented: bool
    recommended_mode: str


class Iso21448SotifSupervisor:
    """
    ISO 21448 (Safety of the Intended Functionality) Denetleyicisi.
    Donanım arızası olmasa dahi güneş parlaması, kamera kirlenmesi, LiDAR tıkanıklığı
    veya yapay zeka kararsızlığı kaynaklı hayalet frenlemeleri ve riskleri önler.
    """

    def __init__(
        self,
        min_lidar_return_ratio: float = 0.25,
        max_camera_glare_ratio: float = 0.60,
        max_allowed_entropy: float = 0.72,
    ) -> None:
        self.min_lidar_ratio = min_lidar_return_ratio
        self.max_glare_ratio = max_camera_glare_ratio
        self.max_entropy = max_allowed_entropy

    def evaluate_sotif(
        self,
        camera_confidence: float,
        lidar_confirmed: bool,
        camera_glare_ratio: float = 0.05,
        lidar_valid_return_ratio: float = 0.95,
    ) -> SotifAssessment:
        blindness = (
            camera_glare_ratio > self.max_glare_ratio
            or lidar_valid_return_ratio < self.min_lidar_ratio
        )

        # Kamera nesne görüyor fakat LiDAR açık alanda hiçbir yansıma doğrulamıyorsa
        phantom_prevented = False
        if camera_confidence < 0.80 and not lidar_confirmed:
            phantom_prevented = True
            agreement = 0.25
        elif lidar_confirmed:
            agreement = min(1.0, (camera_confidence + 1.0) / 2.0)
        else:
            agreement = camera_confidence * 0.6

        # Shannon entropi yaklaşımıyla algı belirsizliği
        p = max(1e-4, min(1.0 - 1e-4, camera_confidence))
        entropy = -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))

        sotif_safe = (not blindness) and (entropy <= self.max_entropy or lidar_confirmed)
        if not sotif_safe:
            mode = "MRM_SAFE_PULLOVER" if blindness else "CAUTIOUS_SPEED_LIMIT"
        else:
            mode = "NOMINAL_L4"

        return SotifAssessment(
            sotif_safe=sotif_safe,
            sensor_blindness_detected=blindness,
            cross_modal_agreement_score=round(agreement, 4),
            ai_uncertainty_entropy=round(entropy, 4),
            phantom_brake_prevented=phantom_prevented,
            recommended_mode=mode,
        )


# ============================================================================
# 3. UN/ECE R157 & RESMÎ GAZETE ZORUNLU DSSAD / EDR KARA KUTU KAYDEDİCİSİ
# ============================================================================

@dataclass
class DssadEventRecord:
    """Tek bir değiştirilemez DSSAD / EDR adli bilişim kara kutu kaydı."""
    sequence_id: int
    timestamp_ms: int
    event_type: str
    control_authority: str           # "AUTONOMOUS_L4" veya "HUMAN_DRIVER"
    vehicle_speed_kmh: float
    steering_angle_deg: float
    deceleration_mps2: float
    fault_or_trigger_code: str
    prev_hash: str
    record_hash: str


class UnR157DssadBlackbox:
    """
    UN/ECE R157 ve 1 Aralık 2024 Resmî Gazete Tip Onayı Yönetmeliği Uyumlu
    Otonom Sürüş Veri Depolama Sistemi (DSSAD / Kara Kutu).

    Her kritik olayı SHA-256 kriptografik özet zinciriyle mühürler; kayıtların
    sonradan silinmesini veya değiştirilmesini matematiksel olarak imkansız kılar.
    """

    GENESIS_HASH = "0" * 64

    def __init__(self) -> None:
        self.records: List[DssadEventRecord] = []

    def log_event(
        self,
        event_type: str,
        control_authority: str,
        vehicle_speed_kmh: float,
        steering_angle_deg: float,
        deceleration_mps2: float = 0.0,
        fault_or_trigger_code: str = "NONE",
        timestamp_ms: Optional[int] = None,
    ) -> DssadEventRecord:
        seq_id = len(self.records) + 1
        ts_ms = timestamp_ms if timestamp_ms is not None else int(time.time() * 1000)
        prev_h = self.records[-1].record_hash if self.records else self.GENESIS_HASH

        payload_str = (
            f"{seq_id}|{ts_ms}|{event_type}|{control_authority}|"
            f"{vehicle_speed_kmh:.2f}|{steering_angle_deg:.2f}|"
            f"{deceleration_mps2:.2f}|{fault_or_trigger_code}|{prev_h}"
        )
        rec_hash = hashlib.sha256(payload_str.encode("utf-8")).hexdigest()

        record = DssadEventRecord(
            sequence_id=seq_id,
            timestamp_ms=ts_ms,
            event_type=event_type,
            control_authority=control_authority,
            vehicle_speed_kmh=round(vehicle_speed_kmh, 2),
            steering_angle_deg=round(steering_angle_deg, 2),
            deceleration_mps2=round(deceleration_mps2, 2),
            fault_or_trigger_code=fault_or_trigger_code,
            prev_hash=prev_h,
            record_hash=rec_hash,
        )
        self.records.append(record)
        return record

    def verify_chain_integrity(self) -> bool:
        """Tüm kara kutu kayıt zincirinin değiştirilmediğini kriptografik olarak doğrular."""
        expected_prev = self.GENESIS_HASH
        for rec in self.records:
            if rec.prev_hash != expected_prev:
                return False
            payload_str = (
                f"{rec.sequence_id}|{rec.timestamp_ms}|{rec.event_type}|{rec.control_authority}|"
                f"{rec.vehicle_speed_kmh:.2f}|{rec.steering_angle_deg:.2f}|"
                f"{rec.deceleration_mps2:.2f}|{rec.fault_or_trigger_code}|{rec.prev_hash}"
            )
            computed = hashlib.sha256(payload_str.encode("utf-8")).hexdigest()
            if computed != rec.record_hash:
                return False
            expected_prev = rec.record_hash
        return True


# ============================================================================
# 4. SİMÜLASYON (İDEAL) DEĞERLERİ VS. GERÇEK SAHA KALİBRASYON TOLERANS MODELİ
# ============================================================================

@dataclass
class SimulationVsFieldProfile:
    """
    Simülasyon ortamındaki ideal (nominal) metrikler ile fiziksel araç üzerindeki
    beklenen saha kalibrasyon toleranslarını karşılaştıran mühendislik modeli.
    """
    # Simülasyon (İdeal / Nominal) Değerleri
    nominal_self_check_ms: float = 20.0
    nominal_watchdog_timeout_ms: float = 50.0
    nominal_canfd_latency_ms: float = 1.4
    nominal_mrm_pullover_decel_mps2: float = 1.5
    nominal_human_override_ms: float = 5.0

    def compute_field_tolerances(
        self,
        road_friction_mu: float = 0.85,
        can_bus_load_pct: float = 35.0,
    ) -> Dict[str, float]:
        """
        Zemin sürtünme katsayısı (mu) ve CAN veri yolu yüküne göre
        gerçek araç üzerinde beklenen fiziksel saha değerlerini hesaplar.
        """
        mu = max(0.25, min(1.0, road_friction_mu))
        bus_factor = 1.0 + max(0.0, (can_bus_load_pct - 20.0) / 100.0)

        expected_can_latency_ms = round(self.nominal_canfd_latency_ms * bus_factor, 2)
        achievable_pullover_decel_mps2 = round(min(self.nominal_mrm_pullover_decel_mps2, mu * 9.81 * 0.5), 2)
        expected_override_ms = round(self.nominal_human_override_ms + (expected_can_latency_ms - 1.4), 2)

        return {
            "nominal_self_check_ms": self.nominal_self_check_ms,
            "nominal_watchdog_timeout_ms": self.nominal_watchdog_timeout_ms,
            "nominal_canfd_latency_ms": self.nominal_canfd_latency_ms,
            "field_expected_canfd_latency_ms": expected_can_latency_ms,
            "nominal_mrm_pullover_decel_mps2": self.nominal_mrm_pullover_decel_mps2,
            "field_achievable_pullover_decel_mps2": achievable_pullover_decel_mps2,
            "nominal_human_override_ms": self.nominal_human_override_ms,
            "field_expected_human_override_ms": expected_override_ms,
        }
