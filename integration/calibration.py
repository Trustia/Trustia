"""
TRUSTIA Entegrasyon Katmanı - Donanım ve Sensör Kalibrasyon Araçları.

Kabiliyetler:
  * Sensör Dış Parametre (Extrinsics - 3D Dönüşüm) Kalibrasyonu
  * CAN-Bus Direksiyon / Gaz Sinyal Sıfırlama ve Ofset Ayarları
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Tuple, Dict, Any


@dataclass
class SensorExtrinsics:
    """Sensörün araç merkezine (Base Link) göre konumu ve açısı."""
    x_m: float = 0.0
    y_m: float = 0.0
    z_m: float = 0.0
    roll_rad: float = 0.0
    pitch_rad: float = 0.0
    yaw_rad: float = 0.0


class HardwareCalibrator:
    """Sensör ve Sürüş Aktüatörü Kalibrasyon Motoru."""

    def __init__(self) -> None:
        self.sensor_offsets: Dict[str, SensorExtrinsics] = {}

    def set_sensor_offset(self, sensor_name: str, extrinsics: SensorExtrinsics) -> None:
        """Sensör ofset değerini kaydeder."""
        self.sensor_offsets[sensor_name] = extrinsics

    def transform_point_to_vehicle(self, sensor_name: str, point: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """Sensör koordinatındaki bir noktayı araç merkezine (Base Link) dönüştürür."""
        if sensor_name not in self.sensor_offsets:
            return point
        ext = self.sensor_offsets[sensor_name]
        px = point[0] + ext.x_m
        py = point[1] + ext.y_m
        pz = point[2] + ext.z_m
        return (px, py, pz)
