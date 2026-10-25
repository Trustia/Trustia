"""
TRUSTIA Otonomi Platformu — CalmCar CalmDrive 3.0 Emniyet Hakemi & Veri Kalkanı (SDK v2.4).
ISO 26262 ASIL-D Emniyet Hakemi (Safety Arbiter) & KVKK m.9 Uç Güvenlik Kalkanı (Edge-Sealing Firewall).

Horizon Robotics Journey 6 (J6M) & SAIC Maxus MIFA 7 Entegrasyon Modülü.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional


@dataclass
class Obstacle3D:
    """3B Algılanan Engel / Yolcu / Araç."""
    obstacle_id: int
    class_name: str          # "VEHICLE", "PEDESTRIAN", "CYCLIST", "DEBRIS"
    rel_x_m: float           # İleri mesafe (m)
    rel_y_m: float           # Sol/sağ yanal ofset (m)
    rel_vx_mps: float        # Bağıl hız (m/s)
    confidence: float        # Algı güven skoru [0.0 - 1.0]
    is_lidar_confirmed: bool # LiDAR nokta bulutu ile doğrulanma durumu

    @property
    def distance_m(self) -> float:
        return math.hypot(self.rel_x_m, self.rel_y_m)

    @property
    def time_to_collision_s(self) -> float:
        """Çarpışmaya Kalan Zaman (TTC)."""
        if self.rel_x_m > 0 and self.rel_vx_mps < -0.1:
            return abs(self.rel_x_m / self.rel_vx_mps)
        return float("inf")


class CalmCarSafetyArbiter:
    """
    CalmCar Derin Öğrenme Algı Motoru için Deterministik Emniyet Hakemi.
    Yapay zekanın halüsinasyonlarını, hayalet frenlemelerini ve yabancı bulut sızıntılarını engeller.
    """

    def __init__(
        self,
        min_detection_confidence: float = 0.65,
        min_ttc_threshold_s: float = 2.2,
        emergency_ttc_threshold_s: float = 1.1,
        enforce_domestic_edge_sealing: bool = True
    ) -> None:
        self.min_confidence = min_detection_confidence
        self.min_ttc = min_ttc_threshold_s
        self.emergency_ttc = emergency_ttc_threshold_s
        self.enforce_edge_sealing = enforce_domestic_edge_sealing

        # Güvenlik ve mevzuat istatistikleri
        self.blocked_foreign_sync_attempts = 0
        self.quarantined_hallucinations = 0
        self.total_frames_arbitrated = 0

    def evaluate_perception_stream(
        self,
        calmcar_raw_objects: List[Dict[str, any]],
        lidar_ground_truth_clusters: List[Tuple[float, float]]
    ) -> Tuple[List[Obstacle3D], bool, str]:
        """
        CalmCar Horizon J6M algı çıktılarını LiDAR ve deterministik fizik kurallarıyla doğrular.
        Dönüş: (Doğrulanmış Engeller, Emniyet İhlali Var Mı, Durum Raporu)
        """
        self.total_frames_arbitrated += 1
        verified_obstacles: List[Obstacle3D] = []
        requires_immediate_braking = False
        status_msg = "Perception Stream ASIL-D Nominal"

        for raw in calmcar_raw_objects:
            obj_id = raw.get("id", 0)
            c_name = raw.get("class", "UNKNOWN")
            rx = float(raw.get("x", 0.0))
            ry = float(raw.get("y", 0.0))
            rvx = float(raw.get("vx", 0.0))
            conf = float(raw.get("confidence", 0.0))

            # 1. Güven Eşiği ve Fiziksel Tutarlılık Filtresi
            if conf < self.min_confidence:
                self.quarantined_hallucinations += 1
                continue

            # 2. LiDAR Çift-Sensör Çapraz Doğrulaması (Cross-Sensor Validation)
            # Eğer CalmCar nesne görüyor ama LiDAR o koordinatta hiç yansıma almıyorsa hayalet engeldir
            lidar_confirmed = False
            for lx, ly in lidar_ground_truth_clusters:
                if math.hypot(rx - lx, ry - ly) < 1.0: # 1 metre tolerans
                    lidar_confirmed = True
                    break

            # Şehir içi yolcu emniyetinde kamera tek başına yetersizse ve güven < %80 ise izole et
            if not lidar_confirmed and conf < 0.85 and rx > 5.0:
                self.quarantined_hallucinations += 1
                continue

            obs = Obstacle3D(
                obstacle_id=obj_id,
                class_name=c_name,
                rel_x_m=rx,
                rel_y_m=ry,
                rel_vx_mps=rvx,
                confidence=conf,
                is_lidar_confirmed=lidar_confirmed
            )
            verified_obstacles.append(obs)

            # 3. Kritik Çarpışma Emniyet Hakemliği (TTC Arbitrajı)
            ttc = obs.time_to_collision_s
            if ttc < self.emergency_ttc and abs(ry) < 1.4:
                requires_immediate_braking = True
                status_msg = f"CRITICAL HAZARD: TTC {ttc:.2f}s on {c_name} at {rx:.1f}m! Triggering ASIL-D MRM."

        return verified_obstacles, requires_immediate_braking, status_msg

    def inspect_cloud_telemetry_packet(self, destination_ip_or_url: str, packet_size_bytes: int) -> bool:
        """
        CalmCar DataTurbo Uç Güvenlik Kalkanı (Edge-Sealing Firewall).
        KVKK m.9 ve CB Bilgi Güvenliği Genelgesi uyarınca Çin/yurt dışı CalmForge sunucularına
        ham kamera/LiDAR veri akışını engeller, yalnızca Tripy Türkiye yerel sunucularına izin verir.
        """
        if not self.enforce_edge_sealing:
            return True

        allowed_domains = ["tripy.im", "api.tripy.im", "teknokent.tripy", "10.0.", "192.168."]
        is_allowed = any(dom in destination_ip_or_url for dom in allowed_domains)

        if not is_allowed:
            self.blocked_foreign_sync_attempts += 1
            return False # Paket engellendi (Dropped)

        return True # Güvenli yerel paket onaylandı
