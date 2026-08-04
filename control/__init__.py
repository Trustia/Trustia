"""
TRUSTIA Kontrol Modülü — PID denetleyici ve araç dinamik modeli.

İki bileşen:
  * PID denetleyici: baş açısı ve hız hatalarını denetim sinyaline
    çevirir (antivindup korumalı)
  * Araç modeli: diferansiyel (robotik) sürüş modeli — istenen
    hız ve açısal hızdan tekerlek komutları, ve fiziksel sınırlar

Kontrol döngüsü, algı/planlama çıktılarını alıp aktüatör komutları
üretir; güvenlik katmanı aşırı komutları keser.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional, Tuple

from core.errors import ControlError


@dataclass
class PidGains:
    """PID katsayıları."""

    kp: float
    ki: float
    kd: float

    def validate(self) -> None:
        if self.kp < 0.0 or self.ki < 0.0 or self.kd < 0.0:
            raise ControlError("PID katsayıları negatif olamaz")


class PidController:
    """Tek eksenli PID denetleyici (antivindup + türev filtresi).

    Giriş: hedef ve mevcut değer; çıkış: denetim sinyali.
    Zaman adımı (dt) her compute çağrısında verilmelidir.
    """

    def __init__(
        self,
        gains: PidGains,
        output_limit: Optional[Tuple[float, float]] = None,
        integral_limit: Optional[float] = None,
    ) -> None:
        gains.validate()
        self._gains = gains
        self._output_limit = output_limit
        self._integral_limit = (
            integral_limit if integral_limit is not None else 10.0
        )
        self._integral = 0.0
        self._previous_error = 0.0
        self._last_dt: Optional[float] = None

    def reset(self) -> None:
        self._integral = 0.0
        self._previous_error = 0.0
        self._last_dt = None

    def compute(self, setpoint: float, measurement: float, dt: float) -> float:
        if dt <= 0.0:
            raise ControlError(f"zaman adımı pozitif olmalı: {dt}")
        error = setpoint - measurement
        self._integral += error * dt
        if self._integral_limit is not None:
            self._integral = max(
                -self._integral_limit,
                min(self._integral_limit, self._integral),
            )
        derivative = 0.0
        if self._last_dt is not None and self._last_dt > 0.0:
            derivative = (error - self._previous_error) / dt
        output = (
            self._gains.kp * error
            + self._gains.ki * self._integral
            + self._gains.kd * derivative
        )
        if self._output_limit is not None:
            output = max(self._output_limit[0],
                         min(self._output_limit[1], output))
        self._previous_error = error
        self._last_dt = dt
        return output


@dataclass
class VehicleModel:
    """Diferansiyel sürüş aracı modeli — hareket kısıtları."""

    wheel_base_m: float = 0.6
    max_speed_mps: float = 3.0
    max_angular_radps: float = 1.5
    max_accel_mps2: float = 1.2
    max_decel_mps2: float = 2.5

    def validate(self) -> None:
        if self.wheel_base_m <= 0.0:
            raise ControlError("dingil mesafesi pozitif olmalı")
        if self.max_speed_mps <= 0.0:
            raise ControlError("maksimum hız pozitif olmalı")
        if self.max_angular_radps <= 0.0:
            raise ControlError("maksimum açısal hız pozitif olmalı")

    def limit_speed(self, requested_mps: float, current_mps: float,
                    dt: float, direction: int = 1) -> float:
        """İvme sınırına göre uygulanabilir hızı döndürür."""
        if dt <= 0.0:
            raise ControlError(f"zaman adımı pozitif olmalı: {dt}")
        if direction >= 0:
            max_delta = self.max_accel_mps2 * dt
            target = min(requested_mps, self.max_speed_mps)
            return min(current_mps + max_delta, target)
        max_delta = self.max_decel_mps2 * dt
        target = max(requested_mps, 0.0)
        return max(current_mps - max_delta, target)

    def limit_angular(self, requested_radps: float) -> float:
        return max(-self.max_angular_radps,
                   min(self.max_angular_radps, requested_radps))


@dataclass
class DriveCommand:
    """Aktüatörlere gönderilen sürüş komutu."""

    forward_mps: float = 0.0
    angular_radps: float = 0.0

    def clamp(self, model: VehicleModel) -> "DriveCommand":
        return DriveCommand(
            forward_mps=max(-model.max_speed_mps,
                            min(model.max_speed_mps, self.forward_mps)),
            angular_radps=model.limit_angular(self.angular_radps),
        )


class Controller:
    """Baş ve hız denetleyicisini birleştiren üst seviye kontrolör.

    Hedef (baş açısı, hız) girişinden tekerlek seviyesi komut üretir.
    """

    def __init__(
        self,
        model: Optional[VehicleModel] = None,
        heading_gains: Optional[PidGains] = None,
        speed_gains: Optional[PidGains] = None,
    ) -> None:
        self._model = model or VehicleModel()
        self._model.validate()
        self._heading_pid = PidController(
            heading_gains or PidGains(kp=2.0, ki=0.1, kd=0.3),
            output_limit=(-self._model.max_angular_radps,
                          self._model.max_angular_radps),
        )
        self._speed_pid = PidController(
            speed_gains or PidGains(kp=1.0, ki=0.05, kd=0.0),
            output_limit=(0.0, self._model.max_speed_mps),
        )
        self._current_speed = 0.0

    @property
    def current_speed_mps(self) -> float:
        return self._current_speed

    def step(
        self,
        target_heading_rad: float,
        target_speed_mps: float,
        current_heading_rad: float,
        dt: float,
    ) -> DriveCommand:
        """Tek kontrol adımı — güvenli sürüş komutu döndürür."""
        if dt <= 0.0:
            raise ControlError(f"zaman adımı pozitif olmalı: {dt}")
        heading_error = _normalize_angle(target_heading_rad - current_heading_rad)
        angular = self._heading_pid.compute(0.0, -heading_error, dt)
        # Baş hatası büyükse hızı düşür (güvenli dönüş)
        speed_scale = max(0.3, 1.0 - abs(heading_error) / math.pi)
        limited_target = target_speed_mps * speed_scale
        speed = self._speed_pid.compute(limited_target, self._current_speed, dt)
        self._current_speed = self._model.limit_speed(
            speed, self._current_speed, dt)
        command = DriveCommand(
            forward_mps=self._current_speed,
            angular_radps=angular,
        )
        return command.clamp(self._model)

    def emergency_stop(self) -> DriveCommand:
        """Tüm komutları sıfırlar — acil durum kullanımı."""
        self._current_speed = 0.0
        self._heading_pid.reset()
        self._speed_pid.reset()
        return DriveCommand(forward_mps=0.0, angular_radps=0.0)

    def reset(self) -> None:
        """Kontrolörü başlangıç durumuna döndürür (koşular arası temizlik)."""
        self._current_speed = 0.0
        self._heading_pid.reset()
        self._speed_pid.reset()


def _normalize_angle(angle_rad: float) -> float:
    while angle_rad > math.pi:
        angle_rad -= 2.0 * math.pi
    while angle_rad <= -math.pi:
        angle_rad += 2.0 * math.pi
    return angle_rad
