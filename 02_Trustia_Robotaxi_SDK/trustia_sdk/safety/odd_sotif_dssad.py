"""
TRUSTIA Robotaksi SDK — ODD, ISO 21448 (SOTIF) ve UN/ECE R157 DSSAD Kara Kutu Modülü.
1 Aralık 2024 Resmî Gazete Otonom Araç Tip Onayı Yönetmeliği ((AB) 2022/1426) Uyumlu.
"""

from __future__ import annotations

import hashlib
import math
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


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


class OddDomainMonitor:
    """Operasyonel Tasarım Alanı (ODD) ve Coğrafi Çit (Geofence) Denetleyicisi."""

    def __init__(self, config: Optional[OddBoundaryConfig] = None) -> None:
        self.config = config or OddBoundaryConfig()

    def is_inside_geofence(self, x_m: float, y_m: float) -> bool:
        poly = self.config.geofence_polygon_xy
        n = len(poly)
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
    ) -> Tuple[bool, str, float]:
        in_geo = self.is_inside_geofence(x_m, y_m)
        if not in_geo:
            return False, "MRM_SAFE_PULLOVER_GEOFENCE_EXIT", -1.5
        if rainfall_mm_hr > self.config.max_rainfall_mm_per_hr or visibility_m < self.config.min_visibility_m:
            return False, "MRM_SAFE_PULLOVER_WEATHER_ODD_EXIT", -1.5
        if speed_kmh > self.config.max_speed_kmh + 0.5 or abs(road_slope_pct) > self.config.max_road_slope_pct:
            return False, "DEGRADED_SLOWDOWN_ODD_LIMIT", -1.0
        return True, "NOMINAL_ODD_OK", 0.0


class Iso21448SotifSupervisor:
    """ISO 21448 (SOTIF) Sensör Körlüğü, Güneş Parlaması ve Çapraz Doğrulama Hakemi."""

    def __init__(self, min_lidar_ratio: float = 0.25, max_glare_ratio: float = 0.60) -> None:
        self.min_lidar_ratio = min_lidar_ratio
        self.max_glare_ratio = max_glare_ratio

    def evaluate(
        self,
        camera_confidence: float,
        lidar_confirmed: bool,
        camera_glare_ratio: float = 0.05,
        lidar_valid_return_ratio: float = 0.95,
    ) -> Tuple[bool, bool, str]:
        blindness = camera_glare_ratio > self.max_glare_ratio or lidar_valid_return_ratio < self.min_lidar_ratio
        phantom_brake_prevented = (camera_confidence < 0.80 and not lidar_confirmed)
        if blindness:
            return False, phantom_brake_prevented, "MRM_SAFE_PULLOVER_SENSOR_BLINDNESS"
        return True, phantom_brake_prevented, "SOTIF_NOMINAL"


@dataclass
class DssadRecord:
    sequence_id: int
    timestamp_ms: int
    event_type: str
    control_authority: str
    speed_kmh: float
    steer_deg: float
    decel_mps2: float
    prev_hash: str
    record_hash: str


class UnR157DssadBlackbox:
    """UN/ECE R157 & Resmî Gazete Zorunlu Kriptografik SHA-256 Zincirli Kara Kutu."""

    GENESIS_HASH = "0" * 64

    def __init__(self) -> None:
        self.records: List[DssadRecord] = []

    def log_event(
        self,
        event_type: str,
        control_authority: str,
        speed_kmh: float,
        steer_deg: float,
        decel_mps2: float = 0.0,
    ) -> DssadRecord:
        seq = len(self.records) + 1
        ts = int(time.time() * 1000)
        prev_h = self.records[-1].record_hash if self.records else self.GENESIS_HASH
        raw = f"{seq}|{ts}|{event_type}|{control_authority}|{speed_kmh:.2f}|{steer_deg:.2f}|{decel_mps2:.2f}|{prev_h}"
        rec_h = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        rec = DssadRecord(seq, ts, event_type, control_authority, round(speed_kmh, 2), round(steer_deg, 2), round(decel_mps2, 2), prev_h, rec_h)
        self.records.append(rec)
        return rec

    def verify_integrity(self) -> bool:
        expected = self.GENESIS_HASH
        for r in self.records:
            if r.prev_hash != expected:
                return False
            raw = f"{r.sequence_id}|{r.timestamp_ms}|{r.event_type}|{r.control_authority}|{r.speed_kmh:.2f}|{r.steer_deg:.2f}|{r.decel_mps2:.2f}|{r.prev_hash}"
            if hashlib.sha256(raw.encode("utf-8")).hexdigest() != r.record_hash:
                return False
            expected = r.record_hash
        return True
