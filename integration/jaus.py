"""
TRUSTIA Araç/Sensör Entegrasyonu (Sistem 8) — JAUS mesaj katmanı.

PLAN 3.8: "JAUS mesaj seti: AS6091 servisleri (Mobility, Positioning,
Payload)".
SAE AS6009/AS6091 temelli mesaj çerçevesi: sabit boyutlu ikili başlık
(32 bayt) + JSON gövde. Servisler (Mobility, Positioning, Payload)
standart mesaj adlarıyla (SetSpeed, QuerySpeed, ReportPose...) üretilir
ve çözülür; araç komut yüzeyi (core.api) JAUS mesajlarına eşlenir.
"""

from __future__ import annotations

import json
import struct
from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, List, Optional

from core.api import Command, CommandType

# ---- başlık ----

HEADER_FORMAT = "!BBHIIHH16s"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
assert HEADER_SIZE == 32, HEADER_SIZE


class MessageType(IntEnum):
    COMMAND = 1
    QUERY = 2
    REPORT = 3
    INFORM = 4
    ERROR = 5


class ServiceId(IntEnum):
    MOBILITY = 1
    POSITIONING = 2
    PAYLOAD = 3


# ---- servis mesaj kodları ----

class MobilityCode(IntEnum):
    SET_SPEED = 0x0101
    SET_WRENCH = 0x0102
    QUERY_SPEED = 0x0103
    REPORT_SPEED = 0x0104
    REPORT_VELOCITY = 0x0105
    EMERGENCY_STOP = 0x0106
    EMERGENCY_CLEAR = 0x0107
    SET_COURSE = 0x0108
    RETURN_HOME = 0x0109
    START_MISSION = 0x010A
    STOP_MISSION = 0x010B
    PAUSE_MISSION = 0x010C
    RESUME_MISSION = 0x010D


class PositioningCode(IntEnum):
    QUERY_POSE = 0x0201
    REPORT_POSE = 0x0202
    REPORT_POSITION_ORIENTATION = 0x0203


class PayloadCode(IntEnum):
    SET_PAYLOAD_STATE = 0x0301
    QUERY_PAYLOAD = 0x0302
    REPORT_PAYLOAD = 0x0303


@dataclass
class JausMessage:
    """JAUS mesajı: başlık + gövde (payload sözlüğü JSON kodlanır)."""

    message_type: MessageType
    service: ServiceId
    message_code: int
    source_uid: int
    destination_uid: int
    sequence: int = 0
    payload: dict = None

    def __post_init__(self) -> None:
        if self.payload is None:
            self.payload = {}

    def encode(self) -> bytes:
        body = json.dumps(self.payload, sort_keys=True,
                          ensure_ascii=False).encode("utf-8")
        if len(body) > 65535:
            raise ValueError(f"gövde çok büyük: {len(body)} bayt")
        header = struct.pack(
            HEADER_FORMAT,
            int(self.message_type), int(self.service), int(self.message_code),
            self.source_uid, self.destination_uid, self.sequence,
            len(body), b"",
        )
        return header + body

    @classmethod
    def decode(cls, data: bytes) -> "JausMessage":
        if len(data) < HEADER_SIZE:
            raise ValueError(f"kısa JAUS mesajı: {len(data)} bayt")
        (message_type, service, code, source, destination, sequence,
         body_len, _) = struct.unpack(HEADER_FORMAT, data[:HEADER_SIZE])
        body = data[HEADER_SIZE:HEADER_SIZE + body_len]
        payload = json.loads(body.decode("utf-8"))
        return cls(
            message_type=MessageType(message_type),
            service=ServiceId(service),
            message_code=code,
            source_uid=source,
            destination_uid=destination,
            sequence=sequence,
            payload=payload,
        )


class JausEndpoint:
    """Tek JAUS uç noktası (araç/GCS) — gönderim/tüketici arabirimi."""

    def __init__(self, uid: int, name: str = "") -> None:
        self.uid = uid
        self.name = name or f"uydu-{uid}"
        self._sequence = 0
        self._sent: List[JausMessage] = []
        self._received: List[JausMessage] = []

    def new_sequence(self) -> int:
        self._sequence = (self._sequence + 1) & 0xFFFF
        return self._sequence

    def send(self, message: JausMessage) -> bytes:
        message.source_uid = self.uid
        message.sequence = self.new_sequence()
        self._sent.append(message)
        return message.encode()

    def receive(self, data: bytes) -> JausMessage:
        message = JausMessage.decode(data)
        self._received.append(message)
        return message

    def sent_count(self) -> int:
        return len(self._sent)

    def received_count(self) -> int:
        return len(self._received)

    def sent_messages(self) -> List[JausMessage]:
        return list(self._sent)


# ---- AS6091 servisleri ----

class MobilityService:
    """Mobility servisi (AS6009 temelli): hız, yön, görev komutları."""

    def __init__(self, endpoint: JausEndpoint) -> None:
        self._ep = endpoint

    def set_speed(self, destination_uid: int, speed_mps: float) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.COMMAND, ServiceId.MOBILITY, MobilityCode.SET_SPEED,
            self._ep.uid, destination_uid,
            payload={"speed_mps": speed_mps},
        ))

    def set_course(self, destination_uid: int, heading_deg: float) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.COMMAND, ServiceId.MOBILITY, MobilityCode.SET_COURSE,
            self._ep.uid, destination_uid,
            payload={"heading_deg": heading_deg},
        ))

    def query_speed(self, destination_uid: int) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.QUERY, ServiceId.MOBILITY, MobilityCode.QUERY_SPEED,
            self._ep.uid, destination_uid,
        ))

    def report_speed(self, destination_uid: int, speed_mps: float) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.REPORT, ServiceId.MOBILITY, MobilityCode.REPORT_SPEED,
            self._ep.uid, destination_uid,
            payload={"speed_mps": speed_mps},
        ))

    def report_velocity(self, destination_uid: int, vx: float, vy: float,
                        omega: float) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.REPORT, ServiceId.MOBILITY,
            MobilityCode.REPORT_VELOCITY, self._ep.uid, destination_uid,
            payload={"vx_mps": vx, "vy_mps": vy, "omega_radps": omega},
        ))

    def emergency_stop(self, destination_uid: int) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.COMMAND, ServiceId.MOBILITY,
            MobilityCode.EMERGENCY_STOP, self._ep.uid, destination_uid,
        ))

    def emergency_clear(self, destination_uid: int) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.COMMAND, ServiceId.MOBILITY,
            MobilityCode.EMERGENCY_CLEAR, self._ep.uid, destination_uid,
        ))

    def return_home(self, destination_uid: int) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.COMMAND, ServiceId.MOBILITY, MobilityCode.RETURN_HOME,
            self._ep.uid, destination_uid,
        ))


class PositioningService:
    """Positioning servisi: konum/başlangıç raporları."""

    def __init__(self, endpoint: JausEndpoint) -> None:
        self._ep = endpoint

    def query_pose(self, destination_uid: int) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.QUERY, ServiceId.POSITIONING,
            PositioningCode.QUERY_POSE, self._ep.uid, destination_uid,
        ))

    def report_pose(self, destination_uid: int, x_m: float, y_m: float,
                    heading_deg: float, gps_available: bool = False) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.REPORT, ServiceId.POSITIONING,
            PositioningCode.REPORT_POSE, self._ep.uid, destination_uid,
            payload={"x_m": x_m, "y_m": y_m, "heading_deg": heading_deg,
                     "gps": gps_available},
        ))


class PayloadService:
    """Payload servisi (AS6091): yük (modül) durum komutu ve raporu."""

    def __init__(self, endpoint: JausEndpoint) -> None:
        self._ep = endpoint

    def set_payload_state(self, destination_uid: int, state: str,
                          detail: str = "") -> bytes:
        return self._ep.send(JausMessage(
            MessageType.COMMAND, ServiceId.PAYLOAD,
            PayloadCode.SET_PAYLOAD_STATE, self._ep.uid, destination_uid,
            payload={"state": state, "detail": detail},
        ))

    def query_payload(self, destination_uid: int) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.QUERY, ServiceId.PAYLOAD, PayloadCode.QUERY_PAYLOAD,
            self._ep.uid, destination_uid,
        ))

    def report_payload(self, destination_uid: int, state: str) -> bytes:
        return self._ep.send(JausMessage(
            MessageType.REPORT, ServiceId.PAYLOAD,
            PayloadCode.REPORT_PAYLOAD, self._ep.uid, destination_uid,
            payload={"state": state},
        ))


# ---- core.api eşlemesi ----

_COMMAND_CODE_MAP: Dict[CommandType, MobilityCode] = {
    CommandType.SET_SPEED: MobilityCode.SET_SPEED,
    CommandType.SET_HEADING: MobilityCode.SET_COURSE,
    CommandType.EMERGENCY_STOP: MobilityCode.EMERGENCY_STOP,
    CommandType.EMERGENCY_CLEAR: MobilityCode.EMERGENCY_CLEAR,
    CommandType.RETURN_HOME: MobilityCode.RETURN_HOME,
    CommandType.START_MISSION: MobilityCode.START_MISSION,
    CommandType.STOP_MISSION: MobilityCode.STOP_MISSION,
    CommandType.PAUSE_MISSION: MobilityCode.PAUSE_MISSION,
    CommandType.RESUME_MISSION: MobilityCode.RESUME_MISSION,
    CommandType.LOAD_WAYPOINTS: MobilityCode.SET_COURSE,
}


def command_to_message(command: Command, source_uid: int,
                       destination_uid: int) -> JausMessage:
    """core.api komutunu JAUS mesajına eşler (GCS → araç yönü)."""
    code = _COMMAND_CODE_MAP.get(command.command_type)
    if code is None:
        raise ValueError(
            f"JAUS eşlemesi yok: {command.command_type.name}"
        )
    payload = dict(command.params)
    return JausMessage(
        MessageType.COMMAND, ServiceId.MOBILITY, code,
        source_uid, destination_uid, payload=payload,
    )


_CODE_COMMAND_MAP: Dict[MobilityCode, CommandType] = {
    code: ctype for ctype, code in _COMMAND_CODE_MAP.items()
}


def message_to_command(message: JausMessage) -> Command:
    """JAUS mesajını core.api komutuna eşler (araç → GCS yönü)."""
    if message.service != ServiceId.MOBILITY:
        raise ValueError(
            f"komut eşlemesi yalnızca Mobility servisinde: {message.service.name}"
        )
    command_type = _CODE_COMMAND_MAP.get(message.message_code)
    if command_type is None:
        raise ValueError(f"JAUS komut kodu bilinmiyor: {message.message_code:#x}")
    return Command(
        command_id=0,
        command_type=command_type,
        params=dict(message.payload),
        source="jaus",
    )