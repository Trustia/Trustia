"""
TRUSTIA Güvenlik (Sistem 5) — Mesaj kimlik doğrulama katmanı.

PLAN 3.6: "Yetkilendirme: rol tabanlı erişim, şifreleme (TLS)".
Transport düzeyi TLS ile sarılır; uygulama düzeyinde her mesaj
HMAC-SHA256 ile imzalanır (bütünlük + kimlik), zaman pencereli
sayaç yeniden oynatma (replay) saldırısını engeller.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Optional


class SecureMessage:
    """HMAC-SHA256 imzalı, zaman pencereli güvenli mesaj."""

    def __init__(self, key: bytes, clock_skew_s: float = 10.0) -> None:
        if not key:
            raise ValueError("paylaşılan anahtar boş olamaz")
        self._key = key
        self._skew_s = clock_skew_s

    @staticmethod
    def _shared_secret(password: str) -> bytes:
        return hashlib.sha256(password.encode("utf-8")).digest()

    def sign_payload(self, payload: dict,
                     at_s: Optional[float] = None) -> dict:
        """Yükü imzalar; nonce (timestamp tabanlı) yeniden oynatmayı kırar."""
        at_s = at_s if at_s is not None else time.time()
        body = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        canonical = f"{int(at_s * 1000)}|{body}".encode("utf-8")
        signature = hmac.new(self._key, canonical, hashlib.sha256).hexdigest()
        return {
            "payload": payload,
            "ts_ms": int(at_s * 1000),
            "sig": signature,
        }

    def verify(self, envelope: dict,
               now_s: Optional[float] = None) -> Optional[dict]:
        """İmzayı ve zaman penceresini doğrular; geçerse payload döner."""
        payload = envelope.get("payload")
        ts_ms = envelope.get("ts_ms")
        signature = envelope.get("sig")
        if payload is None or ts_ms is None or signature is None:
            return None
        body = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        canonical = f"{ts_ms}|{body}".encode("utf-8")
        expected = hmac.new(self._key, canonical, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, str(signature)):
            return None
        now = now_s if now_s is not None else time.time()
        age_s = abs(now - ts_ms / 1000.0)
        if age_s > self._skew_s:
            return None
        return payload