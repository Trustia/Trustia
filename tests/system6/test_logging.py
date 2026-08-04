"""Sistem 6 — Log motoru birim testleri."""

import io
import os

import pytest

from core.logging import (
    Logger,
    LogLevel,
    StreamHandler,
    RotatingFileHandler,
    create_console_logger,
)


def capture_handler():
    buffer = io.StringIO()
    handler = StreamHandler(buffer)
    return handler, buffer


def test_level_filter_debug_below_min():
    logger = Logger("node", min_level=LogLevel.WARNING)
    handler, buffer = capture_handler()
    logger.add_handler(handler)
    logger.info("mod", "görünmemeli")
    assert buffer.getvalue() == ""


def test_level_filter_meets_min():
    logger = Logger("node", min_level=LogLevel.WARNING)
    handler, buffer = capture_handler()
    logger.add_handler(handler)
    logger.warning("mod", "uyarı")
    assert "uyarı" in buffer.getvalue()


def test_set_level_raises_capture():
    logger = Logger()
    handler, buffer = capture_handler()
    logger.add_handler(handler)
    logger.set_level(LogLevel.ERROR)
    logger.warning("mod", "gizli")
    logger.error("mod", "görünür")
    assert "görünür" in buffer.getvalue()
    assert "gizli" not in buffer.getvalue()


def test_record_format_contains_fields():
    logger = Logger("vehicle-1", min_level=LogLevel.DEBUG)
    handler, buffer = capture_handler()
    logger.add_handler(handler)
    logger.info("navigation", "konum güncellendi")
    line = buffer.getvalue()
    assert "vehicle-1" in line
    assert "INFO" in line
    assert "navigation" in line
    assert "konum güncellendi" in line
    assert "." in line


def test_level_name_visible():
    logger = Logger(min_level=LogLevel.DEBUG)
    handler, buffer = capture_handler()
    logger.add_handler(handler)
    logger.critical("mod", "kritik")
    assert "CRITICAL" in buffer.getvalue()


def test_rotating_file_handler_writes():
    path = os.path.join(os.environ.get("TEMP", "."), "trustia_test_rot.log")
    if os.path.exists(path):
        os.remove(path)
    handler = RotatingFileHandler(path)
    logger = Logger()
    logger.add_handler(handler)
    logger.info("mod", "satır bir")
    handler.close()
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()
    assert "satır bir" in content
    os.remove(path)


def test_rotation_creates_backup():
    base = os.path.join(os.environ.get("TEMP", "."), "trustia_test_rot")
    path = base + ".log"
    for suffix in ("", ".1", ".2"):
        candidate = path if suffix == "" else path + suffix
        if os.path.exists(candidate):
            os.remove(candidate)
    handler = RotatingFileHandler(path, max_bytes=256, backup_count=2)
    logger = Logger()
    logger.add_handler(handler)
    for i in range(100):
        logger.info("mod", f"dolgu satırı {i:04d} çok uzun olsun diye yazıyorum")
    handler.close()
    assert os.path.exists(path)
    for suffix in ("", ".1", ".2"):
        candidate = path if suffix == "" else path + suffix
        if os.path.exists(candidate):
            os.remove(candidate)


def test_create_console_logger_returns_logger():
    logger = create_console_logger("x")
    assert isinstance(logger, Logger)


def test_close_flushes_and_clears_handlers():
    logger = Logger()
    handler, buffer = capture_handler()
    logger.add_handler(handler)
    logger.close()
    logger.info("mod", "kapandıktan sonra")
    assert buffer.getvalue() == ""


def test_parse_level():
    assert LogLevel.parse("debug") == LogLevel.DEBUG
    assert LogLevel.parse(" CRITICAL ") == LogLevel.CRITICAL
    with pytest.raises(ValueError):
        LogLevel.parse("bilinmeyen")
