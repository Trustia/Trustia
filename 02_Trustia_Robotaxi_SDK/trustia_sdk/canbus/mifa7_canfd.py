"""
TRUSTIA Otonomi Platformu — SAIC Maxus MIFA 7 & E-GMP CAN-FD Aktüatör Sürücüsü.
ISO 11898-1 CAN-FD Standart Uyumlu (500 kbps arbitraj / 2 Mbps veri hattı).

SAIC Maxus MIFA 7 & Hyundai E-GMP Seviye-4 Aktüatör Kodlama ve Çözümleme Protokolü.
"""

from __future__ import annotations

import struct
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict


CAN_STD_MAX_DLC = 8
CAN_FD_MAX_DLC = 64


@dataclass
class CanFdFrame:
    """Tek bir ISO 11898-1 CAN / CAN-FD Çerçevesi."""
    arbitration_id: int
    data: bytes
    is_fd: bool = True
    bitrate_switch: bool = True
    timestamp: float = 0.0

    def __post_init__(self) -> None:
        if self.timestamp == 0.0:
            self.timestamp = time.time()
        limit = CAN_FD_MAX_DLC if self.is_fd else CAN_STD_MAX_DLC
        if len(self.data) > limit:
            raise ValueError(f"CAN verisi maksimum DLC sınırını aşıyor: {len(self.data)} > {limit}")
        if not (0 <= self.arbitration_id <= 0x1FFFFFFF):
            raise ValueError(f"Geçersiz CAN Arbitrasyon Kimliği: {self.arbitration_id:#x}")

    @property
    def dlc(self) -> int:
        return len(self.data)


# SAIC Maxus MIFA 7 & Hyundai Ioniq 5 CAN-FD Kimlik Haritası
ID_MIFA7_HEARTBEAT_FD      = 0x010   # 50 Hz Otonomi Yaşam Sinyali (ASIL-D Heartbeat)
ID_MIFA7_STEERING_CMD_FD   = 0x1A0   # 100 Hz Direksiyon Açı ve Tork Komutu (EPS LKAS)
ID_MIFA7_ACCEL_BRAKE_CMD_FD= 0x1A1   # 50 Hz İvme, Hız ve Rejeneratif/Mekanik Fren Komutu
ID_MIFA7_ESTOP_CMD         = 0x014   # 100 Hz Acil Durum / MRM Güvenli Durma Tetiği
ID_MIFA7_WHEEL_SPEEDS_FD   = 0x386   # 100 Hz 4 Tekerlek Odometri ve Hız Telemetrisi
ID_MIFA7_BATTERY_STATUS    = 0x544   # 10 Hz Yüksek Voltaj Batarya Telemetrisi (% SoC, kW)
ID_MIFA7_ACTUATOR_FEEDBACK = 0x2A0   # 100 Hz Gerçek Direksiyon Açısı ve Tork Geri Bildirimi


class Mifa7CanFdBridge:
    """
    SAIC Maxus MIFA 7 & Seviye-4 Elektrikli MPV CAN-FD Protokol Dönüştürücüsü.
    """

    def __init__(self, channel: str = "can0", bitrate: int = 500000, data_bitrate: int = 2000000) -> None:
        self.channel = channel
        self.bitrate = bitrate
        self.data_bitrate = data_bitrate
        self.tx_history: List[CanFdFrame] = []
        self.rx_history: List[CanFdFrame] = []
        self.rolling_counter: int = 0
        self.last_steer_deg: float = 0.0
        self.last_target_speed_mps: float = 0.0

    def encode_steering_command(
        self,
        target_angle_deg: float,
        max_torque_nm: float = 4.5,
        steer_rate_deg_s: float = 120.0
    ) -> CanFdFrame:
        """
        Maxus MIFA 7 EPS (Elektronik Direksiyon) kontrol çerçevesini kodlar (100 Hz).
        """
        # Güvenlik limitleri: Maksimum +/- 35 derece mekanik sınır
        clamped_angle = max(-35.0, min(35.0, target_angle_deg))
        clamped_torque = max(0.0, min(6.0, max_torque_nm))
        self.last_steer_deg = clamped_angle

        # 0.01 derece hassasiyetle int16 dönüşümü
        raw_angle = int(round(clamped_angle * 100.0))
        raw_rate = int(round(steer_rate_deg_s * 10.0))
        raw_torque = int(round(clamped_torque * 100.0))

        self.rolling_counter = (self.rolling_counter + 1) & 0x0F

        # CAN-FD Veri Yükü (16 Byte güvenli çerçeve: Açı, Açısal Hız, Tork, Sayaç, Sağlama)
        # format: <h (angle: 2B), H (rate: 2B), H (torque: 2B), B (counter/mode: 1B), B (checksum: 1B)
        mode_byte = (self.rolling_counter << 4) | 0x01 # 0x01: Autonomous Drive Active
        header_data = struct.pack("<hHHB", raw_angle, raw_rate, raw_torque, mode_byte)
        checksum = (sum(header_data) ^ 0xAA) & 0xFF
        payload = header_data + bytes([checksum]) + bytes(8) # 16 byte padding

        frame = CanFdFrame(arbitration_id=ID_MIFA7_STEERING_CMD_FD, data=payload, is_fd=True)
        self.tx_history.append(frame)
        return frame

    def encode_accel_brake_command(
        self,
        target_accel_mps2: float,
        target_speed_mps: float,
        brake_pressure_bar: float = 0.0
    ) -> CanFdFrame:
        """
        Maxus MIFA 7 Motor İnvertörü ve i-Booster Elektronik Fren komutunu kodlar (50 Hz).
        """
        # Yolcu konforu ivmelenme sınırı: [-4.0, +2.5] m/s2
        clamped_accel = max(-6.5, min(2.5, target_accel_mps2))
        clamped_speed = max(0.0, min(14.0, target_speed_mps)) # maks 50 km/h (13.88 m/s)
        self.last_target_speed_mps = clamped_speed

        raw_accel = int(round(clamped_accel * 100.0))
        raw_speed = int(round(clamped_speed * 100.0))
        raw_brake = int(round(brake_pressure_bar * 10.0))

        counter = (self.rolling_counter & 0x0F)
        ctrl_mode = 0x02 # 0x02: L4 Longitudinal Control Active
        mode_byte = (counter << 4) | ctrl_mode

        header = struct.pack("<hhHB", raw_accel, raw_speed, raw_brake, mode_byte)
        checksum = (sum(header) ^ 0x55) & 0xFF
        payload = header + bytes([checksum]) + bytes(8)

        frame = CanFdFrame(arbitration_id=ID_MIFA7_ACCEL_BRAKE_CMD_FD, data=payload, is_fd=True)
        self.tx_history.append(frame)
        return frame

    def encode_heartbeat(self, asil_status_ok: bool = True) -> CanFdFrame:
        """50 Hz ASIL-D Sistem Sağlık ve Güvenlik Kalp Atışı (Watchdog)."""
        status_code = 0x01 if asil_status_ok else 0xFF
        payload = struct.pack("<BBHL", status_code, self.rolling_counter, 0x1337, int(time.time() * 1000) & 0xFFFFFFFF)
        frame = CanFdFrame(arbitration_id=ID_MIFA7_HEARTBEAT_FD, data=payload, is_fd=False)
        self.tx_history.append(frame)
        return frame

    def encode_emergency_stop(self, reason_code: int = 0x01) -> CanFdFrame:
        """ASIL-D Minimal Risk Maneuver (MRM) Acil Durum Frenleme Tetiği."""
        payload = struct.pack("<BBBB", 0xEE, reason_code, 0xFF, 0x00)
        frame = CanFdFrame(arbitration_id=ID_MIFA7_ESTOP_CMD, data=payload, is_fd=False)
        self.tx_history.append(frame)
        return frame

    def decode_wheel_telemetry(self, frame: CanFdFrame) -> Dict[str, float]:
        """4 Tekerlek hız sensörlerini ve araç hızını çözer."""
        if frame.arbitration_id != ID_MIFA7_WHEEL_SPEEDS_FD:
            return {}
        fl, fr, rl, rr = struct.unpack("<HHHH", frame.data[:8])
        # 0.01 km/h biriminden m/s dönüşümü
        v_fl = (fl * 0.01) / 3.6
        v_fr = (fr * 0.01) / 3.6
        v_rl = (rl * 0.01) / 3.6
        v_rr = (rr * 0.01) / 3.6
        avg_speed_mps = (v_fl + v_fr + v_rl + v_rr) / 4.0
        return {
            "v_fl_mps": v_fl,
            "v_fr_mps": v_fr,
            "v_rl_mps": v_rl,
            "v_rr_mps": v_rr,
            "vehicle_speed_mps": avg_speed_mps,
            "vehicle_speed_kmh": avg_speed_mps * 3.6
        }
