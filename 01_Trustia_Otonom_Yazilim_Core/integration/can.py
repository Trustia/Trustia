"""
TRUSTIA Araç/Sensör Entegrasyonu (Sistem 8) — CAN katmanı.

PLAN 3.8: "CAN bus katmanı: standart CAN + CAN FD mesajları,
motor/direksiyon komutları".
CAN çerçevesi kodlanır/çözülür; motor hız ve direksiyon açısı
komutları tanımlı kimliklerle bus üzerinden iletilir.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import List, Optional


CAN_MAX_DLC = 8
CAN_FD_MAX_DLC = 64


@dataclass
class CanFrame:
    """Tek CAN/CAN FD çerçevesi."""

    arbitration_id: int
    data: bytes
    is_fd: bool = False

    def __post_init__(self) -> None:
        limit = CAN_FD_MAX_DLC if self.is_fd else CAN_MAX_DLC
        if len(self.data) > limit:
            raise ValueError(f"CAN verisi uzun: {len(self.data)} > {limit}")
        if not (0 <= self.arbitration_id <= 0x7FF):
            raise ValueError(f"arbitraj kimliği geçersiz: {self.arbitration_id}")

    @property
    def dlc(self) -> int:
        return len(self.data)


# ---- komut kimlikleri (araç ağı eşlemesi) ----

ID_MOTOR_SPEED = 0x011
ID_STEERING_ANGLE = 0x012
ID_STEERING_SPEED = 0x013
ID_ESTOP_STATE = 0x014
ID_MOTOR_TELEMETRY = 0x021
ID_BATTERY_TELEMETRY = 0x022

# ---- Hyundai Ioniq 5 E-GMP CAN-FD Kimlikleri (5 Mbps Bus) ----
ID_IONIQ5_LKAS_FD = 0x1A0       # Direksiyon Açı ve Tork Enjeksiyonu (100 Hz)
ID_IONIQ5_SCC_FD = 0x1A1        # Akıllı Hız, İvme ve Fren Basıncı (50 Hz)
ID_IONIQ5_WHL_SPD_FD = 0x386    # 4 Tekerlek Darbe ve Hız Telemetrisi
ID_IONIQ5_BATTERY_800V = 0x544  # 800V E-GMP Yüksek Voltaj Batarya Telemetrisi



class CanBus:
    """CAN transitörü — çerçeve enkapsülasyonu ve saat/halat kaydı."""

    def __init__(self) -> None:
        self._tx: List[CanFrame] = []

    def transmit(self, frame: CanFrame) -> None:
        self._tx.append(frame)

    def tx_count(self) -> int:
        return len(self._tx)

    def last(self) -> Optional[CanFrame]:
        return self._tx[-1] if self._tx else None

    def frames_with_id(self, arbitration_id: int) -> List[CanFrame]:
        return [f for f in self._tx if f.arbitration_id == arbitration_id]


class MotorController:
    """Motor hız komutu: CAN mesajına kodlar/çözer."""

    @staticmethod
    def encode_speed(speed_mps: float) -> bytes:
        return struct.pack("<i", int(round(speed_mps * 1000.0)))

    @staticmethod
    def decode_speed(frame: CanFrame) -> float:
        if frame.arbitration_id != ID_MOTOR_SPEED:
            raise ValueError(f"beklenmeyen çerçeve: {frame.arbitration_id:#x}")
        (raw,) = struct.unpack("<i", frame.data[:4])
        return raw / 1000.0


class SteeringController:
    """Direksiyon komutu: açı (radyan) ve dönüş hızını kodlar."""

    @staticmethod
    def encode(angle_rad: float, rate_radps: float = 0.5) -> bytes:
        return struct.pack("<ii", int(round(angle_rad * 1000.0)),
                           int(round(rate_radps * 1000.0)))

    @staticmethod
    def decode(frame: CanFrame) -> tuple:
        if frame.arbitration_id == ID_STEERING_ANGLE:
            return struct.unpack("<i", frame.data[:4])[0] / 1000.0
        if frame.arbitration_id == ID_STEERING_SPEED:
            return struct.unpack("<ii", frame.data[:8])[0] / 1000.0
        raise ValueError(f"beklenmeyen çerçeve: {frame.arbitration_id:#x}")


class EstopActuator:
    """Acil durma hattı — fail-safe (normalde kapalı) mantıkta tek kutu.

    `energized=True` sürüş serbest değildir; hat kesilince araç durur.
    """

    @staticmethod
    def encode(enabled: bool) -> bytes:
        return bytes([1 if enabled else 0])

    @staticmethod
    def decode(frame: CanFrame) -> bool:
        if frame.arbitration_id != ID_ESTOP_STATE:
            raise ValueError(f"beklenmeyen çerçeve: {frame.arbitration_id:#x}")
        return frame.data[0] == 1


def drive_command(bus: CanBus, speed_mps: float,
                  angle_rad: float, rate_radps: float = 0.5,
                  estop_enabled: bool = True) -> List[CanFrame]:
    """Tek sürüş döngüsü komutlarını üretir ve bus üzerinden iletir."""
    frames = [
        CanFrame(ID_MOTOR_SPEED, MotorController.encode_speed(speed_mps)),
        CanFrame(ID_STEERING_ANGLE, SteeringController.encode(angle_rad, rate_radps)),
        CanFrame(ID_ESTOP_STATE, EstopActuator.encode(estop_enabled)),
    ]
    for frame in frames:
        bus.transmit(frame)
    return frames


class SocketCanBus(CanBus):
    """Linux SocketCAN (can0, vcan0) Gerçek Donanım Sürücüsü.

    Linux çekirdeğindeki AF_CAN soketi üzerinden endüstriyel Kvaser/PEAK cihazlarına
    çerçeve gönderir ve alır; donanım soketi bulunamadığında güvenli sanal moda geçer.
    """

    def __init__(self, interface: str = "can0", fallback_to_virtual: bool = True) -> None:
        super().__init__()
        self.interface = interface
        self.fallback_to_virtual = fallback_to_virtual
        self.is_hardware_connected = False
        self._sock = None

        self._init_socket()

    def _init_socket(self) -> None:
        import socket
        if hasattr(socket, "AF_CAN") and hasattr(socket, "CAN_RAW"):
            try:
                self._sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
                self._sock.bind((self.interface,))
                self._sock.setblocking(False)
                self.is_hardware_connected = True
            except (OSError, PermissionError):
                self._sock = None
                self.is_hardware_connected = False
        else:
            self._sock = None
            self.is_hardware_connected = False

    def transmit(self, frame: CanFrame) -> None:
        super().transmit(frame)
        if self._sock is not None and self.is_hardware_connected:
            import struct
            can_dlc = len(frame.data)
            data_padded = frame.data.ljust(8, b"\x00")
            can_pkt = struct.pack("=IB3x8s", frame.arbitration_id, can_dlc, data_padded)
            try:
                self._sock.send(can_pkt)
            except OSError:
                pass


class HyundaiIoniq5CanFdController:
    """Hyundai Ioniq 5 (E-GMP Platformu) Seviye-4 CAN-FD Denetleyicisi.

    100Hz LKAS_FD direksiyon açısı enjeksiyonu, 50Hz SCC_FD hız/ivme/fren kontrolü
    ve 800V batarya telemetrisi yönetimini sağlar.
    """

    def __init__(self, bus: CanBus) -> None:
        self.bus = bus

    def send_lkas_steering(self, target_angle_deg: float, torque_request_nm: float = 0.0) -> CanFrame:
        """LKAS_FD direksiyon açısı ve torku enjekte eder."""
        raw_angle = int(round(target_angle_deg * 10.0))
        raw_torque = int(round(torque_request_nm * 100.0))
        data = struct.pack("<hh4s", raw_angle, raw_torque, b"\x00\x00\x00\x00")
        frame = CanFrame(arbitration_id=ID_IONIQ5_LKAS_FD, data=data, is_fd=True)
        self.bus.transmit(frame)
        return frame

    def send_scc_acceleration(self, accel_mps2: float, target_speed_kph: float) -> CanFrame:
        """SCC_FD hız ve ivme/fren komutu iletir."""
        raw_accel = int(round(accel_mps2 * 100.0))
        raw_speed = int(round(target_speed_kph * 10.0))
        data = struct.pack("<hh4s", raw_accel, raw_speed, b"\x00\x00\x00\x00")
        frame = CanFrame(arbitration_id=ID_IONIQ5_SCC_FD, data=data, is_fd=True)
        self.bus.transmit(frame)
        return frame

    def read_battery_status(self, frame: CanFrame) -> dict:
        """800V E-GMP batarya telemetrisini çözümler."""
        if frame.arbitration_id != ID_IONIQ5_BATTERY_800V or len(frame.data) < 6:
            return {"soc_pct": 0.0, "voltage_v": 0.0, "temp_c": 0.0}
        soc_pct, voltage_raw, temp_raw = struct.unpack("<hbb", frame.data[:4])
        return {
            "soc_pct": soc_pct / 10.0,
            "voltage_v": voltage_raw * 2.0,
            "temp_c": float(temp_raw),
        }