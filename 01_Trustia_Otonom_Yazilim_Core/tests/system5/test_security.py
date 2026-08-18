"""Sistem 5 — Güvenlik katmanı birim testleri.

Acil durma anahtarı protokolü, bağlantı kaybı yönetimi (dur → bekle →
geri dön), komut doğrulama, denetim kaydı ve mesaj imzalama (HMAC).
"""

from __future__ import annotations

import pytest

from security import Shield
from security.audit import AuditLog
from security.crypto import SecureMessage
from security.estop import EmergencyStop, EstopState
from security.linkloss import LinkLossManager, LinkState
from security.validate import CommandGuard


# ------------------------------------------------------------- Estop


def test_estop_initial_normal():
    estop = EmergencyStop()
    assert estop.state == EstopState.NORMAL
    assert estop.vehicle_enabled()


def test_estop_stop_disables_driving():
    estop = EmergencyStop()
    estop.stop("fiziksel", message="buton")
    assert estop.state == EstopState.STOPPED
    assert not estop.vehicle_enabled()
    assert not estop.stopped is False
    assert estop.stopped


def test_estop_clear_reenables():
    estop = EmergencyStop()
    estop.stop("yazılımsal")
    estop.clear("operatör")
    assert estop.state == EstopState.NORMAL
    assert estop.vehicle_enabled()


def test_estop_hardware_fault_blocks_clear():
    estop = EmergencyStop()
    estop.hardware_fault("arayüz")
    estop.clear("operatör")
    assert estop.state == EstopState.HARDWARE_FAULT
    assert not estop.vehicle_enabled()


def test_estop_events_recorded():
    estop = EmergencyStop()
    estop.stop("fiziksel")
    estop.clear("operatör")
    events = estop.events()
    assert len(events) == 2
    assert events[0].action == "stop"
    assert events[0].source == "fiziksel"
    assert events[1].action == "clear"


def test_estop_listener_receives_events():
    estop = EmergencyStop()
    received = []

    class Listener:
        def on_estop(self, event):
            received.append(event.action)

    estop.attach(Listener())
    estop.stop("test")
    assert received == ["stop"]


def test_estop_repeated_stop_is_idempotent():
    estop = EmergencyStop()
    estop.stop("a")
    estop.stop("b")
    assert len(estop.events()) == 1


# ---------------------------------------------------------- Linkloss


def test_linkloss_nominal_while_frames_arrive():
    manager = LinkLossManager(lost_after_s=2.0)
    for t in range(0, 20):
        manager.on_frame(t)
        assert manager.evaluate(t).action == ""
    assert manager.state == LinkState.NOMINAL


def test_linkloss_stops_after_gap():
    manager = LinkLossManager(lost_after_s=1.0, safe_stop_s=1.0)
    manager.on_frame(0.0)
    manager.evaluate(2.5)
    decision = manager.evaluate(3.5)
    assert decision.action == "stop"
    assert decision.is_safe_stop
    assert manager.state == LinkState.STOPPED


def test_linkloss_returns_home_after_wait():
    manager = LinkLossManager(
        lost_after_s=0.1, safe_stop_s=0.1, wait_before_return_s=0.5
    )
    manager.on_frame(0.0)
    for t in range(0, 20):
        manager.evaluate(t / 10)
    assert manager.state == LinkState.RETURNING
    assert manager.return_requested()


def test_linkloss_reconnect_recovers():
    manager = LinkLossManager(lost_after_s=0.1, safe_stop_s=0.1)
    manager.on_frame(0.0)
    manager.evaluate(0.5)
    manager.evaluate(1.5)
    assert manager.state == LinkState.STOPPED
    manager.on_frame(0.6)
    assert manager.state == LinkState.NOMINAL


def test_linkloss_invalid_params_rejected():
    with pytest.raises(ValueError):
        LinkLossManager(lost_after_s=0.0)


# ---------------------------------------------------------- Validate


def test_guard_speed_limits():
    guard = CommandGuard(max_speed_mps=2.5)
    assert guard.validate_speed(2.0).valid
    assert not guard.validate_speed(3.0).valid
    assert not guard.validate_speed(-0.1).valid


def test_guard_heading_bounds():
    guard = CommandGuard()
    assert guard.validate_heading(180.0).valid
    assert not guard.validate_heading(361.0).valid
    assert not guard.validate_heading(-1.0).valid


def test_guard_target_world_bounds():
    guard = CommandGuard(world_bounds_m=(40.0, 40.0))
    assert guard.validate_target(20.0, 30.0).valid
    assert not guard.validate_target(45.0, 10.0).valid
    assert not guard.validate_target(10.0, -2.0).valid


def test_guard_clearance():
    guard = CommandGuard(min_clearance_m=0.3)
    assert guard.validate_clearance(1.0).valid
    assert not guard.validate_clearance(0.1).valid


def test_guard_speed_command_blocked_during_emergency():
    guard = CommandGuard()
    assert not guard.validate_speed_command(1.0, emergency=True).valid


def test_guard_speed_command_with_clearance():
    guard = CommandGuard()
    assert guard.validate_speed_command(1.0, clearance_m=1.5).valid
    assert not guard.validate_speed_command(2.8, clearance_m=1.5).valid


# -------------------------------------------------------------- Audit


def test_audit_records_query(tmp_path):
    with AuditLog(str(tmp_path), "test") as audit:
        audit.record("op", "start_mission", "G-1", "onaylandı")
        audit.record("admin", "estop", "A-01")
        audit.record("op", "start_mission", "G-2")
    assert audit.count() == 3
    by_user = audit.query(user="op")
    assert len(by_user) == 2
    by_action = audit.query(action="estop")
    assert len(by_action) == 1


def test_audit_writes_file(tmp_path):
    audit = AuditLog(str(tmp_path), "kayit")
    audit.record("admin", "open")
    audit.close()
    content = (tmp_path / "kayit.jsonl").read_text(encoding="utf-8")
    assert '"action": "open"' in content


# ------------------------------------------------------------- Crypto


def test_secure_message_sign_verify_roundtrip():
    secure = SecureMessage(b"sifre-anahtar")
    envelope = secure.sign_payload({"hız": 1.5, "hedef": [10, 20]})
    assert secure.verify(envelope) == {"hız": 1.5, "hedef": [10, 20]}


def test_secure_message_tamper_detected():
    secure = SecureMessage(b"sifre-anahtar")
    envelope = secure.sign_payload({"hız": 1.5})
    envelope["payload"]["hız"] = 9.9
    assert secure.verify(envelope) is None


def test_secure_message_wrong_key_rejected():
    secure = SecureMessage(b"dogru-anahtar")
    forged = SecureMessage(b"yanlis-anahtar")
    envelope = forged.sign_payload({"v": 1.0})
    assert secure.verify(envelope) is None


def test_secure_message_replay_rejected():
    secure = SecureMessage(b"sifre-anahtar")
    envelope = secure.sign_payload({"v": 1.0}, at_s=100.0)
    assert secure.verify(envelope, now_s=200.0) is None
    assert secure.verify(envelope, now_s=100.0) is not None


# ------------------------------------------------------------- Shield


def test_shield_emergency_and_audit(tmp_path):
    shield = Shield(tmp_path, link_key=b"anahtar")
    shield.emergency_stop("fiziksel")
    assert not shield.vehicle_enabled()
    shield.emergency_clear("operatör")
    assert shield.vehicle_enabled()
    events = shield.audit_query(action="emergency_stop")
    assert len(events) == 1
    assert events[0]["user"] == "shield"
    shield.close()


def test_shield_validate_command_rejects(tmp_path):
    shield = Shield(tmp_path)
    shield.estop.stop("test")
    result = shield.validate_command("op", "goto", speed_mps=1.0)
    assert not result.valid
    shield.close()


def test_shield_sign_requires_key(tmp_path):
    shield = Shield(tmp_path)
    with pytest.raises(RuntimeError):
        shield.sign_message({"a": 1})
    shield.close()


def test_shield_link_frame_flow(tmp_path):
    shield = Shield(tmp_path, lost_after_s=0.2, safe_stop_s=0.1,
                    wait_before_return_s=0.4)
    for t in range(0, 30):
        if t % 3 == 0:
            shield.link_frame(t)
        decision = shield.evaluate_link(t / 10)
    assert decision.action in ("RETURN_HOME", "stop", "")
    shield.close()