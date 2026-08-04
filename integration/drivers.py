"""
TRUSTIA Araç/Sensör Entegrasyonu (Sistem 8) — Sürücü soyutlaması.

PLAN 3.8: "LiDAR sürücüleri: çok marka soyutlama arayüzü";
"Kamera sürücüleri: USB/GigE, renk/termal".
Marka/sensör bağımsız ortak arayüz; donanım katmanı yalnızca
arayüzle konuşur.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class LidarPoint:
    """LiDAR dönüş noktası (aracın yerel çerçevesinde)."""

    angle_rad: float
    range_m: float
    intensity: float = 0.0


class LidarDriver(ABC):
    """Çok marka LiDAR için ortak sürücü arayüzü."""

    @abstractmethod
    def scan(self) -> Sequence[LidarPoint]:
        """Tek dönüşlük nokta bulutu döndürür."""

    @abstractmethod
    def model_name(self) -> str:
        ...


class _SimulatedLidarSource(LidarDriver):
    """Sanal LiDAR — simülasyon dünyasına köprü (donanımsız test için)."""

    def __init__(self, source) -> None:
        self._source = source

    def scan(self):
        return self._source

    def model_name(self) -> str:
        return "simülasyon"

    def point_cloud(self) -> Sequence[LidarPoint]:
        return list(self._source)


class RotaryLidarDriver(LidarDriver):
    """Sanal tabanlı model (mock): gözetleme ölçeği/çözünürlüğü doğrular."""

    def __init__(self, base: Sequence[LidarPoint] = ()) -> None:
        self._base = list(base)
        self._scan_count = 0

    def feed(self, points: Sequence[LidarPoint]) -> None:
        self._base = list(points)

    def scan(self) -> Sequence[LidarPoint]:
        self._scan_count += 1
        return list(self._base)

    def model_name(self) -> str:
        return "rotary-v2"

    def scan_count(self) -> int:
        return self._scan_count


@dataclass
class CameraFrame:
    """Kamera karesi meta verisi (piksel verisi uygulamada opsiyonel)."""

    width: int
    height: int
    channels: int
    thermal: bool = False
    source: str = ""


class CameraDriver(ABC):
    """USB/GigE kamera sürücü arayüzü — renk ve termal ortak çatı."""

    @abstractmethod
    def capture(self) -> CameraFrame:
        ...

    @abstractmethod
    def interface(self) -> str:
        ...


class GigEStagCamera(CameraDriver):
    """Renkli, GigE bağlantılı kamera (mock)."""

    def __init__(self, width: int = 1280, height: int = 720) -> None:
        self._size = (width, height)

    def capture(self) -> CameraFrame:
        return CameraFrame(*self._size, channels=3, source="GigE")

    def interface(self) -> str:
        return "GigE"


class UsbThermalCamera(CameraDriver):
    """Termal kamera — gece görüşü; tek kanal 16-bit sıcaklık (mock)."""

    def __init__(self, width: int = 640, height: int = 512) -> None:
        self._size = (width, height)

    def capture(self) -> CameraFrame:
        return CameraFrame(*self._size, channels=1, thermal=True, source="USB")

    def interface(self) -> str:
        return "USB"