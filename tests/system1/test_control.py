"""Sistem 1 — Kontrol (PID, araç modeli, sürüş komutları) birim testleri."""

import math

import pytest

from core.errors import ControlError
from control import (
    PidController,
    PidGains,
    VehicleModel,
    DriveCommand,
    Controller,
)


def test_pid_reaches_setpoint():
    pid = PidController(PidGains(kp=1.0, ki=0.0, kd=0.0))
    output = pid.compute(10.0, 0.0, dt=0.1)
    assert output == pytest.approx(10.0)


def test_pid_error_sign():
    pid = PidController(PidGains(kp=1.0, ki=0.0, kd=0.0))
    assert pid.compute(0.0, 5.0, dt=0.1) == pytest.approx(-5.0)


def test_pid_integral_builds_up():
    pid = PidController(PidGains(kp=0.0, ki=1.0, kd=0.0))
    total = 0.0
    for _ in range(5):
        total += pid.compute(10.0, 0.0, dt=0.1)
    assert total > 0.0


def test_pid_antiwindup():
    pid = PidController(
        PidGains(kp=1.0, ki=10.0, kd=0.0), integral_limit=2.0
    )
    for _ in range(100):
        pid.compute(10.0, 0.0, dt=0.1)
    # integral limiti nedeniyle çıktı sınırlanmalı
    assert pid.compute(10.0, 0.0, dt=0.1) <= 30.0


def test_pid_output_limit():
    pid = PidController(
        PidGains(kp=5.0, ki=0.0, kd=0.0), output_limit=(-1.0, 1.0)
    )
    assert pid.compute(10.0, 0.0, dt=0.1) == pytest.approx(1.0)
    assert pid.compute(-10.0, 0.0, dt=0.1) == pytest.approx(-1.0)


def test_pid_negative_gains_rejected():
    with pytest.raises(ControlError):
        PidController(PidGains(kp=-1.0, ki=0.0, kd=0.0))


def test_pid_negative_dt_rejected():
    pid = PidController(PidGains(kp=1.0, ki=0.0, kd=0.0))
    with pytest.raises(ControlError):
        pid.compute(1.0, 0.0, dt=-0.1)


def test_pid_reset_clears_state():
    pid = PidController(PidGains(kp=0.0, ki=1.0, kd=0.0))
    for _ in range(10):
        pid.compute(10.0, 0.0, dt=0.1)
    pid.reset()
    assert pid.compute(10.0, 0.0, dt=0.1) == pytest.approx(1.0)


def test_vehicle_model_limits_speed():
    model = VehicleModel(max_speed_mps=3.0, max_accel_mps2=1.0)
    assert model.limit_speed(10.0, 0.0, dt=0.5) == pytest.approx(0.5)


def test_vehicle_model_caps_at_max():
    model = VehicleModel(max_speed_mps=3.0, max_accel_mps2=10.0)
    assert model.limit_speed(100.0, 0.0, dt=0.5) == pytest.approx(3.0)


def test_vehicle_model_deceleration():
    model = VehicleModel(max_decel_mps2=2.0)
    assert model.limit_speed(0.0, 5.0, dt=0.5, direction=-1) == pytest.approx(4.0)


def test_vehicle_model_angular_limit():
    model = VehicleModel(max_angular_radps=1.5)
    assert model.limit_angular(5.0) == pytest.approx(1.5)
    assert model.limit_angular(-5.0) == pytest.approx(-1.5)


def test_vehicle_model_validation():
    with pytest.raises(ControlError):
        VehicleModel(wheel_base_m=0.0).validate()


def test_drive_command_clamp():
    model = VehicleModel(max_speed_mps=3.0, max_angular_radps=1.5)
    clamped = DriveCommand(forward_mps=10.0, angular_radps=9.0).clamp(model)
    assert clamped.forward_mps == pytest.approx(3.0)
    assert clamped.angular_radps == pytest.approx(1.5)


def test_controller_heading_follow():
    controller = Controller()
    command = controller.step(
        target_heading_rad=math.pi / 2,
        target_speed_mps=1.0,
        current_heading_rad=0.0,
        dt=0.1,
    )
    # sağa dönüş komutu
    assert command.angular_radps > 0.0
    assert command.forward_mps >= 0.0


def test_controller_heading_negative():
    controller = Controller()
    command = controller.step(
        target_heading_rad=-math.pi / 2,
        target_speed_mps=1.0,
        current_heading_rad=0.0,
        dt=0.1,
    )
    assert command.angular_radps < 0.0


def test_controller_speed_limited():
    controller = Controller()
    controller.step(math.pi / 2, 1.0, 0.0, dt=0.1)
    assert controller.current_speed_mps <= 3.0


def test_controller_emergency_stop():
    controller = Controller()
    controller.step(math.pi / 2, 2.0, 0.0, dt=0.5)
    command = controller.emergency_stop()
    assert command.forward_mps == 0.0
    assert command.angular_radps == 0.0
    assert controller.current_speed_mps == 0.0


def test_controller_negative_dt_rejected():
    controller = Controller()
    with pytest.raises(ControlError):
        controller.step(0.0, 1.0, 0.0, dt=0.0)
