"""Sistem 6 — Ayar sistemi birim testleri."""

import json
import os

import pytest

from core.config import Config, ConfigError


def temp_config_path(data: dict) -> str:
    path = os.path.join(
        os.environ.get("TEMP", "."), "trustia_test_cfg.json"
    )
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    return path


def test_defaults_applied():
    cfg = Config(defaults={"vehicle.max_speed": 5.0})
    assert cfg.get_float("vehicle.max_speed") == 5.0


def test_nested_merge_flattens():
    cfg = Config({"a": {"b": {"c": 1}}})
    assert cfg.get("a.b.c") == 1


def test_load_file_merges():
    path = temp_config_path({"vehicle": {"max_speed": 7.5}, "mode": "auto"})
    cfg = Config()
    cfg.load_file(path)
    assert cfg.get_float("vehicle.max_speed") == 7.5
    assert cfg.get_str("mode") == "auto"
    os.remove(path)


def test_load_file_missing_raises():
    cfg = Config()
    with pytest.raises(ConfigError):
        cfg.load_file("yok_olan_dosya.json")


def test_load_file_invalid_json_raises():
    path = os.path.join(os.environ.get("TEMP", "."), "trustia_bad.json")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("{ geçersiz json")
    cfg = Config()
    with pytest.raises(ConfigError):
        cfg.load_file(path)
    os.remove(path)


def test_override_wins_over_file():
    path = temp_config_path({"speed": 1.0})
    cfg = Config(defaults={"speed": 0.5})
    cfg.load_file(path)
    cfg.apply_overrides({"speed": 9.9})
    assert cfg.get_float("speed") == 9.9
    os.remove(path)


def test_env_load(monkeypatch):
    monkeypatch.setenv("TRUSTIA_VEHICLE__MAX_SPEED", "12.5")
    monkeypatch.setenv("TRUSTIA_TELEMETRY__ENABLED", "true")
    monkeypatch.setenv("TRUSTIA_NAME", "barkan")
    cfg = Config()
    cfg.load_env()
    assert cfg.get_float("vehicle.max_speed") == 12.5
    assert cfg.get_bool("telemetry.enabled") is True
    assert cfg.get_str("name") == "barkan"


def test_require_missing_raises():
    cfg = Config()
    with pytest.raises(ConfigError):
        cfg.require("yok")


def test_require_present_ok():
    cfg = Config({"k": 5})
    assert cfg.require("k") == 5


def test_type_enforcement():
    cfg = Config({"s": "on", "i": "7", "l": "a,b,c"})
    assert cfg.get_bool("s") is True
    assert cfg.get_int("i") == 7
    assert cfg.get_list("l") == ["a", "b", "c"]

def test_bad_number_raises():
    cfg = Config({"x": "metin"})
    with pytest.raises(ConfigError):
        cfg.get_float("x")


def test_validate_required():
    cfg = Config({"a": 1})
    cfg.validate_required(["a"])
    with pytest.raises(ConfigError):
        cfg.validate_required(["a", "b"])


def test_as_dict_flat():
    cfg = Config({"a": {"b": 2}})
    assert cfg.as_dict() == {"a.b": 2}
