"""Sistem 8 — Araç/Sensör entegrasyonu birim testleri.

CAN/CAN FD katmanı (motor/direksiyon komutları), çok marka LiDAR ve
kamera sürücü soyutlaması, donanım soyutlama katmanı ve JAUS
(AS6009/AS6091 temelli) mesaj katmanı + core.api komut eşlemesi.
"""

from __future__ import annotations

import pytest

from core.api import Command, CommandType
from integration import (
    CanBus,
    CanFrame,
    EstopActuator,
    GigEStagCamera,
    JausEndpoint,
    JausMessage,
    MessageType,
    MobilityCode,
    MobilityService,
    MotorController,
    PayloadCode,
    PayloadService,
    PositioningCode,
    PositioningService,
    RotaryLidarDriver,
    ServiceId,
    SteeringController,
    UsbThermalCamera,
    VehicleHardware,
    command_to_message,
    drive_command,
    message_to_command,
)
from integration.drivers import LidarPoint


# ---------------------------------------------------------------- CAN


def test_can_frame_dlc_limits():
    CanFrame(0x011, b"\x00" * 8)
    CanFrame(0x011, b"\x00" * 64, is_fd=True)
    with pytest.raises(ValueError):
        CanFrame(0x011, b"\x00" * 9)
    with pytest.raises(ValueError):
        CanFrame(0x800, b"\x00")


def test_motor_speed_roundtrip():
    frame = CanFrame(0x011, MotorController.encode_speed(1.35))
    assert MotorController.decode_speed(frame) == 1.35


def test_steering_angle_roundtrip():
    frame = CanFrame(0x012, SteeringController.encode(0.25, 0.7))
    assert SteeringController.decode(frame) == 0.25


def test_estop_actuator_roundtrip():
    frame = CanFrame(0x014, EstopActuator.encode(True))
    assert EstopActuator.decode(frame) is True
    frame2 = CanFrame(0x014, EstopActuator.encode(False))
    assert EstopActuator.decode(frame2) is False


def test_can_bus_tracks_transmissions():
    bus = CanBus()
    frames = drive_command(bus, 1.5, 0.3, estop_enabled=True)
    assert len(frames) == 3
    assert bus.tx_count() == 3
    assert len(bus.frames_with_id(0x011)) == 1


# ------------------------------------------------------------ Drivers


def test_rotary_lidar_driver_returns_fed_points():
    driver = RotaryLidarDriver()
    points = [LidarPoint(angle_rad=0.0, range_m=2.0),
              LidarPoint(angle_rad=1.0, range_m=3.0)]
    driver.feed(points)
    scan = driver.scan()
    assert len(scan) == 2
    assert scan[1].range_m == 3.0
    assert driver.scan_count() == 1
    assert driver.model_name() == "rotary-v2"


def test_camera_drivers_interface():
    gige = GigEStagCamera()
    frame = gige.capture()
    assert frame.channels == 3
    assert not frame.thermal
    assert gige.interface() == "GigE"
    thermal = UsbThermalCamera()
    tframe = thermal.capture()
    assert tframe.thermal
    assert tframe.channels == 1
    assert thermal.interface() == "USB"


# --------------------------------------------------------- Hardware


def test_hardware_sensor_summary():
    hardware = VehicleHardware(
        lidar=RotaryLidarDriver(),
        cameras=[GigEStagCamera(), UsbThermalCamera()],
    )
    summary = hardware.sensor_summary()
    assert summary["lidar"] == "rotary-v2"
    assert len(summary["cameras"]) == 2


def test_hardware_drive_sends_can_frames():
    hardware = VehicleHardware(lidar=RotaryLidarDriver())
    frames = hardware.drive(1.0, 0.2)
    assert len(frames) == 3
    assert hardware.tx_count() == 3


def test_hardware_acquire_scan_empty_without_lidar():
    hardware = VehicleHardware()
    assert hardware.acquire_scan() == []
    assert not hardware.has_lidar()


# ------------------------------------------------------------ JAUS


def _endpoints():
    gcs = JausEndpoint(0x1001, "GCS")
    araç = JausEndpoint(0x2001, "ARAÇ")
    return gcs, araç


def test_jaus_header_size_32():
    from integration.jaus import HEADER_SIZE
    assert HEADER_SIZE == 32


def test_jaus_set_speed_roundtrip():
    gcs, araç = _endpoints()
    raw = MobilityService(gcs).set_speed(araç.uid, 1.5)
    message = araç.receive(raw)
    assert message.service == ServiceId.MOBILITY
    assert message.message_code == MobilityCode.SET_SPEED
    assert message.message_type == MessageType.COMMAND
    assert message.payload == {"speed_mps": 1.5}
    assert message.destination_uid == araç.uid


def test_jaus_query_report_speed():
    gcs, araç = _endpoints()
    query = MobilityService(gcs).query_speed(araç.uid)
    message = araç.receive(query)
    assert message.message_type == MessageType.QUERY
    report = MobilityService(araç).report_speed(gcs.uid, 2.0)
    report_msg = gcs.receive(report)
    assert report_msg.payload == {"speed_mps": 2.0}


def test_jaus_sequence_increments():
    gcs, araç = _endpoints()
    mobility = MobilityService(gcs)
    first = mobility.set_speed(araç.uid, 1.0)
    second = mobility.set_speed(araç.uid, 1.0)
    assert first[12:14] != second[12:14]


def test_jaus_positioning_pose():
    gcs, araç = _endpoints()
    raw = PositioningService(araç).report_pose(gcs.uid, 3.5, 7.0, 12.0)
    message = gcs.receive(raw)
    assert message.service == ServiceId.POSITIONING
    assert message.message_code == PositioningCode.REPORT_POSE
    assert message.payload["x_m"] == 3.5


def test_jaus_payload_service():
    gcs, araç = _endpoints()
    raw = PayloadService(gcs).set_payload_state(araç.uid, "armed", "kamera")
    message = araç.receive(raw)
    assert message.service == ServiceId.PAYLOAD
    assert message.message_code == PayloadCode.SET_PAYLOAD_STATE
    assert message.payload["state"] == "armed"


def test_jaus_decode_garbage_rejected():
    gcs = JausEndpoint(1)
    with pytest.raises(ValueError):
        gcs.receive(b"kisa")


def test_jaus_inform_type():
    gcs, araç = _endpoints()
    raw = PositioningService(araç).report_pose(gcs.uid, 0.0, 0.0, 0.0)
    message = JausMessage.decode(raw)
    assert message.message_type == MessageType.REPORT


# ------------------------------------------------- Command mapping


def test_command_to_message_emergency_stop():
    command = Command(command_id=1, command_type=CommandType.EMERGENCY_STOP)
    message = command_to_message(command, source_uid=0x1001,
                                 destination_uid=0x2001)
    assert message.message_code == MobilityCode.EMERGENCY_STOP
    assert message.service == ServiceId.MOBILITY
    assert message.source_uid == 0x1001
    assert message.destination_uid == 0x2001


def test_message_to_command_roundtrip():
    gcs, araç = _endpoints()
    command = Command(command_id=5, command_type=CommandType.SET_SPEED,
                      params={"speed_mps": 1.2})
    message = command_to_message(command, gcs.uid, araç.uid)
    converted = message_to_command(message)
    assert converted.command_type == CommandType.SET_SPEED
    assert converted.params == {"speed_mps": 1.2}


def test_message_to_command_unknown_code_rejected():
    message = JausMessage(
        MessageType.QUERY, ServiceId.MOBILITY, 0x9999, 1, 2
    )
    with pytest.raises(ValueError):
        message_to_command(message)


def test_command_to_message_payload_service_rejected():
    command = Command(command_id=1, command_type=CommandType.STANDUP)
    with pytest.raises(ValueError):
        command_to_message(command, 1, 2)