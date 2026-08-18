"""Sistem 6 — Hata hiyerarşisi birim testleri."""

import pytest

from core.errors import (
    TrustiaError,
    RecoverableError,
    ConfigurationError,
    SensorError,
    CommunicationError,
    NavigationError,
    ControlError,
    PlanningError,
    SafetyError,
    ErrorSeverity,
)


def test_hierarchy_assignments():
    assert issubclass(RecoverableError, TrustiaError)
    assert issubclass(ConfigurationError, TrustiaError)
    assert issubclass(SensorError, RecoverableError)
    assert issubclass(CommunicationError, RecoverableError)
    assert issubclass(NavigationError, RecoverableError)
    assert issubclass(ControlError, RecoverableError)
    assert issubclass(PlanningError, RecoverableError)
    assert issubclass(SafetyError, TrustiaError)


def test_recoverable_flag():
    assert RecoverableError("x").recoverable is True
    assert TrustiaError("x").recoverable is False
    assert SensorError("x").recoverable is True


def test_safety_flag():
    error = SafetyError("acil durma")
    assert error.safety_critical is True
    assert error.severity == ErrorSeverity.SAFETY


def test_severity_order():
    assert ErrorSeverity.RECOVERABLE < ErrorSeverity.FATAL < ErrorSeverity.SAFETY


def test_describe_includes_class_and_message():
    error = NavigationError("rota yok", details="koordinat boş")
    text = error.describe()
    assert "NavigationError" in text
    assert "rota yok" in text
    assert "detay" in text


def test_message_stored():
    error = ControlError("aktüatör arızası")
    assert str(error) == "aktüatör arızası"
    assert error.message == "aktüatör arızası"


def test_details_optional():
    error = TrustiaError("basit")
    assert error.details is None
    assert "detay" not in error.describe()


def test_catch_all_as_exception():
    with pytest.raises(Exception):
        raise SafetyError("test")


def test_catch_specific():
    with pytest.raises(ConfigurationError):
        raise ConfigurationError("eksik ayar")
