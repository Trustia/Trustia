"""
TRUSTIA Log Motoru — Seviyeli, döngülü, milisaniye zaman damgalı kayıt sistemi.

Özellikler:
  * Log seviyeleri: DEBUG, INFO, WARNING, ERROR, CRITICAL
  * Birden fazla çıkış hedefi (dosya, konsol, sarmalayıcı)
  * Dosya döngüsü (rotasyon): boyut ve adet sınırı
  * Yapılandırılmış alanlar (zaman, seviye, düğüm, modül)
  * İş parçacığı güvenli yazım
"""

from __future__ import annotations

import os
import sys
import threading
import time
from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional, TextIO


class LogLevel(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    @classmethod
    def parse(cls, name: str) -> "LogLevel":
        normalized = name.strip().upper()
        try:
            return cls[normalized]
        except KeyError:
            raise ValueError(f"geçersiz log seviyesi: {name!r}")


class LogHandler:
    """Log çıktısı hedeflerinin ortak arayüzü."""

    def emit(self, record: "LogRecord") -> None: ...

    def close(self) -> None: ...


class StreamHandler(LogHandler):
    """Metin çıktısını bir akışa (dosya/konsol) yazar."""

    def __init__(self, stream: TextIO) -> None:
        self._stream = stream
        self._lock = threading.Lock()

    def emit(self, record: "LogRecord") -> None:
        line = record.format_line() + "\n"
        with self._lock:
            self._stream.write(line)
            self._stream.flush()

    def close(self) -> None:
        try:
            self._stream.flush()
        except Exception:
            pass


class RotatingFileHandler(LogHandler):
    """Belirtilen boyutu aşınca dosyayı döndüren dosya loglayıcısı.

    max_bytes aşılınca mevcut dosya .1, .2 ... adlarıyla arşivlenir
    ve yeni dosya açılır; backup_count adedinden fazla arşiv silinir.
    """

    def __init__(
        self,
        path: str,
        max_bytes: int = 5 * 1024 * 1024,
        backup_count: int = 3,
    ) -> None:
        self._path = path
        self._max_bytes = max(1024, max_bytes)
        self._backup_count = max(0, backup_count)
        self._lock = threading.Lock()
        self._file = self._open_stream()

    def _open_stream(self) -> TextIO:
        return open(self._path, "a", encoding="utf-8")

    def emit(self, record: "LogRecord") -> None:
        line = record.format_line() + "\n"
        with self._lock:
            self._rotate_if_needed(len(line))
            self._file.write(line)
            self._file.flush()

    def _rotate_if_needed(self, incoming: int) -> None:
        try:
            size = os.path.getsize(self._path)
        except OSError:
            size = 0
        if size + incoming <= self._max_bytes:
            return
        self._file.close()
        for index in range(self._backup_count, 0, -1):
            source = f"{self._path}.{index - 1}" if index > 1 else self._path
            target = f"{self._path}.{index}"
            if os.path.exists(source):
                if os.path.exists(target):
                    os.remove(target)
                os.rename(source, target)
        self._file = self._open_stream()

    def close(self) -> None:
        with self._lock:
            try:
                self._file.close()
            except Exception:
                pass


@dataclass
class LogRecord:
    """Tek bir log kaydının yapılandırılmış içeriği."""

    timestamp_ns: int
    level: LogLevel
    node_id: str
    module: str
    message: str

    def format_line(self) -> str:
        ts = self.timestamp_ns / 1_000_000_000
        stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
        millis = int((self.timestamp_ns % 1_000_000_000) / 1_000_000)
        return (
            f"{stamp}.{millis:03d} "
            f"[{self.level.name:8s}] "
            f"{self.node_id} "
            f"{self.module}: {self.message}"
        )


class Logger:
    """TRUSTIA loglayıcısı — seviye filtreli, çok hedefli, güvenli."""

    def __init__(
        self,
        node_id: str = "trustia",
        min_level: LogLevel = LogLevel.INFO,
    ) -> None:
        self._node_id = node_id
        self._min_level = min_level
        self._handlers: List[LogHandler] = []
        self._lock = threading.Lock()

    def add_handler(self, handler: LogHandler) -> None:
        with self._lock:
            self._handlers.append(handler)

    def set_level(self, level: LogLevel) -> None:
        self._min_level = level

    def _log(self, level: LogLevel, module: str, message: str) -> None:
        if level < self._min_level:
            return
        record = LogRecord(
            timestamp_ns=time.time_ns(),
            level=level,
            node_id=self._node_id,
            module=module,
            message=message,
        )
        with self._lock:
            handlers = list(self._handlers)
        for handler in handlers:
            try:
                handler.emit(record)
            except Exception:
                pass

    def debug(self, module: str, message: str) -> None:
        self._log(LogLevel.DEBUG, module, message)

    def info(self, module: str, message: str) -> None:
        self._log(LogLevel.INFO, module, message)

    def warning(self, module: str, message: str) -> None:
        self._log(LogLevel.WARNING, module, message)

    def error(self, module: str, message: str) -> None:
        self._log(LogLevel.ERROR, module, message)

    def critical(self, module: str, message: str) -> None:
        self._log(LogLevel.CRITICAL, module, message)

    def close(self) -> None:
        with self._lock:
            handlers = list(self._handlers)
            self._handlers.clear()
        for handler in handlers:
            try:
                handler.close()
            except Exception:
                pass


def create_console_logger(
    node_id: str = "trustia",
    min_level: LogLevel = LogLevel.INFO,
) -> Logger:
    """Standart çıktıya yazan hazır loglayıcı döndürür."""
    logger = Logger(node_id=node_id, min_level=min_level)
    logger.add_handler(StreamHandler(sys.stdout))
    return logger
