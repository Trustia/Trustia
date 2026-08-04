"""
TRUSTIA Ayar Sistemi — Öncelik zincirli yapılandırma katmanı.

Öncelik zinciri (düşükten yükseğe):
  1. Varsayılanlar (kod içi)
  2. Yapılandırma dosyası (JSON)
  3. Çevre değişkenleri (TRUSTIA_ öneki)
  4. Komut satırı sözlüğü (programatik/argv)

Özellikler:
  * İç içe (noktalı) anahtar erişimi: "vehicle.max_speed"
  * Tip güvenli okuma: int, float, bool, str, list
  * Bölüm bazında doğrulama
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional

from core.errors import TrustiaError

_ENV_PREFIX = "TRUSTIA_"


class ConfigError(TrustiaError):
    """Ayar sistemi hataları."""


class Config:
    """Katmanlı yapılandırma deposu.

    Örnek kullanım::

        cfg = Config()
        cfg.load_file("config.json")
        speed = cfg.get_float("vehicle.max_speed", default=5.0)
    """

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._values: Dict[str, Any] = {}
        if defaults:
            self._merge(defaults)

    def _merge(self, data: Dict[str, Any], prefix: str = "") -> None:
        for key, value in data.items():
            full = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                self._merge(value, full)
            else:
                self._values[full] = value

    def load_file(self, path: str) -> None:
        """JSON yapılandırma dosyasını zincire ekler."""
        if not os.path.isfile(path):
            raise ConfigError(f"yapılandırma dosyası bulunamadı: {path}")
        try:
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except json.JSONDecodeError as exc:
            raise ConfigError(f"geçersiz JSON: {path}: {exc}")
        if not isinstance(data, dict):
            raise ConfigError(f"yapılandırma kökü nesne olmalı: {path}")
        self._merge(data)

    def load_env(self, prefix: str = _ENV_PREFIX) -> None:
        """TRUSTIA_ önekli ortam değişkenlerini zincire ekler.

        TRUSTIA_VEHICLE_MAX_SPEED=12.5  ->  vehicle.max_speed = 12.5
        """
        for key, value in os.environ.items():
            if not key.startswith(prefix):
                continue
            remainder = key[len(prefix):]
            parts = remainder.lower().split("__")
            dotted = ".".join(parts)
            self._values[dotted] = self._coerce(value)

    def apply_overrides(self, overrides: Dict[str, Any]) -> None:
        """En yüksek öncelikli değerleri (komut satırı/argv) uygular."""
        self._merge(overrides)

    @staticmethod
    def _coerce(value: str) -> Any:
        lower = value.lower()
        if lower in ("true", "yes", "1"):
            return True
        if lower in ("false", "no", "0"):
            return False
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        if "," in value:
            return [item.strip() for item in value.split(",")]
        return value

    def get(self, key: str, default: Any = None) -> Any:
        return self._values.get(key, default)

    def require(self, key: str) -> Any:
        """Anahtar yoksa ConfigError fırlatır."""
        if key not in self._values:
            raise ConfigError(f"gerekli ayar eksik: {key}")
        return self._values[key]

    def get_float(self, key: str, default: float = 0.0) -> float:
        value = self.get(key, default)
        try:
            return float(value)
        except (TypeError, ValueError):
            raise ConfigError(f"{key} bir sayı olmalı, alınan: {value!r}")

    def get_int(self, key: str, default: int = 0) -> int:
        value = self.get(key, default)
        try:
            return int(value)
        except (TypeError, ValueError):
            raise ConfigError(f"{key} bir tam sayı olmalı, alınan: {value!r}")

    def get_bool(self, key: str, default: bool = False) -> bool:
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ("true", "yes", "on", "1")
        raise ConfigError(f"{key} bir bool olmalı, alınan: {value!r}")

    def get_str(self, key: str, default: str = "") -> str:
        value = self.get(key, default)
        if value is None:
            return default
        return str(value)

    def get_list(self, key: str, default: Optional[List[Any]] = None) -> List[Any]:
        value = self.get(key, default if default is not None else [])
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        if isinstance(value, (list, tuple)):
            return list(value)
        raise ConfigError(f"{key} bir liste olmalı, alınan: {value!r}")

    def as_dict(self) -> Dict[str, Any]:
        """Tüm ayarların düzleştirilmiş kopyasını döndürür."""
        return dict(self._values)

    def validate_required(self, keys: List[str]) -> None:
        missing = [key for key in keys if key not in self._values]
        if missing:
            raise ConfigError(f"eksik zorunlu ayarlar: {', '.join(missing)}")
