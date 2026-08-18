"""
TRUSTIA Araç/Sensör Entegrasyonu (Sistem 8) — Donanım soyutlama katmanı.

PLAN 3.8: "Donanım soyutlama katmanı: sensörlerden bağımsız algı".
Algı katmanı yalnızca bu arayüzle konuşur; sürücü (marka) ve fiziksel
bus (CAN) ayrıntıları donanım nesnesinin arkasında saklanır.
"""

from __future__ import annotations

from typing import List, Optional, Sequence

from integration.can import (
    CanBus,
    CanFrame,
    EstopActuator,
    ID_ESTOP_STATE,
    MotorController,
    SteeringController,
)
from integration.drivers import CameraDriver, LidarDriver, LidarPoint


class VehicleHardware:
    """Araç üzerindeki tüm sensör/aktüatörlerin tek soyutlaması."""

    def __init__(
        self,
        lidar: Optional[LidarDriver] = None,
        cameras: Optional[Sequence[CameraDriver]] = None,
    ) -> None:
        self.lidar = lidar
        self.cameras = list(cameras or [])
        self.bus = CanBus()
        self._estop_energized = True

    # ---- algı tarafı ----

    def acquire_scan(self) -> Sequence[LidarPoint]:
        """Algı zincirinin kullandığı tek LiDAR girişi (marka bağımsız)."""
        if self.lidar is None:
            return []
        return self.lidar.scan()

    def acquire_camera(self, index: int = 0) -> Optional[object]:
        if not self.cameras:
            return None
        return self.cameras[index % len(self.cameras)].capture()

    def has_lidar(self) -> bool:
        return self.lidar is not None

    def sensor_summary(self) -> dict:
        return {
            "lidar": self.lidar.model_name() if self.lidar else "yok",
            "cameras": [
                {"source": c.interface(),
                 "thermal": self.cameras and hasattr(c, "capture")}
                for c in self.cameras
            ] if self.cameras else [],
        }

    # ---- aktüatör tarafı ----

    def drive(self, speed_mps: float, angle_rad: float,
              rate_radps: float = 0.5) -> List[CanFrame]:
        """Sürüş komutunu CAN bus üzerinden iletir."""
        frames = [
            CanFrame(0x011, MotorController.encode_speed(speed_mps)),
            CanFrame(0x012, SteeringController.encode(angle_rad, rate_radps)),
            CanFrame(ID_ESTOP_STATE, EstopActuator.encode(self._estop_energized)),
        ]
        for frame in frames:
            self.bus.transmit(frame)
        return frames

    def set_estop_energized(self, enabled: bool) -> None:
        """Emniyet hattı: enerjili iken sürüş serbest, kesilince durur."""
        self._estop_energized = enabled

    def estop_energized(self) -> bool:
        return self._estop_energized

    def tx_count(self) -> int:
        return self.bus.tx_count()
