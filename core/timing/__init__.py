"""
TRUSTIA Zaman Motoru — Monoton saat, periyodik zamanlayıcı ve ölçüm aracı.

Özellikler:
  * Monoton saat (zaman sıçramalarından etkilenmez)
  * Dönem (cycle) sayaçları — zamanlayıcı kaç kez ateşlendi
  * Gecikme (latency) takibi — zamanlama sapması
  * Periyodik zamanlayıcı — sistem döngülerini ateşler
  * Basit süreölçer (stopwatch) — zamanlama ölçümü
"""

from __future__ import annotations

import threading
import time
from typing import Callable, Optional


class MonotonicClock:
    """Nanometre çözünürlüklü monoton saat."""

    @staticmethod
    def now_ns() -> int:
        return time.time_ns()

    @staticmethod
    def now_s() -> float:
        return time.perf_counter()


class Timer:
    """Belirli bir periyotta tekrarlanan döngü tetikleyicisi.

    Her periyot sonunda callback çağrılır; cycle sayacı artar.
    Dönem gecikmesi (drift) biriktirilmez; gerçek hedef zaman her
    periyotta yeniden hesaplanır.
    """

    def __init__(
        self,
        period_s: float,
        callback: Callable[[int], None],
        start_immediately: bool = False,
    ) -> None:
        if period_s <= 0.0:
            raise ValueError(f"periyot pozitif olmalı: {period_s}")
        self._period_s = period_s
        self._callback = callback
        self._running = False
        self._cycle = 0
        self._lock = threading.Lock()
        self._thread: Optional[threading.Thread] = None
        self._start_immediately = start_immediately
        self._last_fire_ns = 0
        self._max_latency_ns = 0

    def start(self) -> None:
        with self._lock:
            if self._running:
                return
            self._running = True
            self._cycle = 0
            self._last_fire_ns = MonotonicClock.now_ns()
            self._max_latency_ns = 0
            self._thread = threading.Thread(
                target=self._run, name="trustia-timer", daemon=True
            )
            self._thread.start()

    def stop(self) -> None:
        with self._lock:
            self._running = False
        thread = self._thread
        if thread is not None:
            thread.join(timeout=max(2.0, self._period_s * 2.0))
        self._thread = None

    def _run(self) -> None:
        while True:
            with self._lock:
                if not self._running:
                    return
            cycle = self._cycle
            self._cycle += 1
            if cycle == 0 and not self._start_immediately:
                continue
            start_ns = MonotonicClock.now_ns()
            try:
                self._callback(cycle)
            except Exception:
                pass
            elapsed_ns = MonotonicClock.now_ns() - start_ns
            with self._lock:
                if elapsed_ns > self._max_latency_ns:
                    self._max_latency_ns = elapsed_ns
                self._last_fire_ns = MonotonicClock.now_ns()
            sleep_s = self._period_s - elapsed_ns / 1e9
            if sleep_s > 0:
                time.sleep(sleep_s)
            else:
                time.sleep(0.0)

    @property
    def cycle(self) -> int:
        with self._lock:
            return self._cycle

    @property
    def running(self) -> bool:
        with self._lock:
            return self._running

    @property
    def max_latency_ns(self) -> int:
        with self._lock:
            return self._max_latency_ns

    @property
    def last_fire_ns(self) -> int:
        with self._lock:
            return self._last_fire_ns

    def elapsed_since_last_fire(self) -> float:
        with self._lock:
            last = self._last_fire_ns
        return (MonotonicClock.now_ns() - last) / 1e9


class Stopwatch:
    """Kod bölümlerinin süresini ölçmek için stopwatch."""

    def __init__(self) -> None:
        self._start_ns: Optional[int] = None

    def start(self) -> None:
        self._start_ns = MonotonicClock.now_ns()

    def elapsed_ns(self) -> int:
        if self._start_ns is None:
            return 0
        return MonotonicClock.now_ns() - self._start_ns

    def elapsed_s(self) -> float:
        return self.elapsed_ns() / 1e9

    def reset(self) -> None:
        self._start_ns = MonotonicClock.now_ns()


class RateLimiter:
    """Saniyede en fazla N kez geçişe izin veren kapı."""

    def __init__(self, max_rate_hz: float) -> None:
        if max_rate_hz <= 0.0:
            raise ValueError(f"oran pozitif olmalı: {max_rate_hz}")
        self._min_interval_ns = int(1e9 / max_rate_hz)
        self._last_pass_ns = 0

    def allow(self) -> bool:
        now = MonotonicClock.now_ns()
        if now - self._last_pass_ns >= self._min_interval_ns:
            self._last_pass_ns = now
            return True
        return False

    def wait(self) -> None:
        while not self.allow():
            time.sleep(0.001)
