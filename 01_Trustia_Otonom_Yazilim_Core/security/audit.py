"""
TRUSTIA Güvenlik (Sistem 5) — Denetim kaydı.

PLAN 3.6: "Denetim kaydı: her komut ve olay kaydı, kim-yaptı-ne-zaman".
JSONL dosyasına akış yazılır; sorgular (kullanıcıya, olaya göre)
desteklenir.
"""

from __future__ import annotations

import json
import os
import time
from typing import Dict, List, Optional


class AuditLog:
    """Denetim kaydı — her olay tek satır JSON olarak saklanır."""

    def __init__(self, directory: str, log_name: str = "denetim") -> None:
        self.directory = directory
        os.makedirs(directory, exist_ok=True)
        self.path = os.path.join(directory, f"{log_name}.jsonl")
        self._entries: List[dict] = []
        self._file = open(self.path, "a", encoding="utf-8")

    def record(self, user: str, action: str, target: str = "",
               detail: str = "", at_ns: Optional[int] = None) -> None:
        entry = {
            "at_ns": at_ns if at_ns is not None else time.time_ns(),
            "user": user,
            "action": action,
            "target": target,
            "detail": detail,
        }
        self._entries.append(entry)
        self._file.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self._file.flush()

    def query(self, user: Optional[str] = None,
              action: Optional[str] = None,
              limit: int = 100) -> List[dict]:
        results = self._entries
        if user is not None:
            results = [e for e in results if e["user"] == user]
        if action is not None:
            results = [e for e in results if e["action"] == action]
        return results[-limit:]

    def count(self) -> int:
        return len(self._entries)

    def close(self) -> None:
        if not self._file.closed:
            self._file.close()

    def __enter__(self) -> "AuditLog":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()