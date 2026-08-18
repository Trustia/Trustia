"""Sistem 6 — Zaman motoru birim testleri."""

import time

import pytest

from core.timing import (
    MonotonicClock,
    Timer,
    Stopwatch,
    RateLimiter,
)


def test_monotonic_clock_advances():
    t1 = MonotonicClock.now_ns()
    time.sleep(0.002)
    t2 = MonotonicClock.now_ns()
    assert t2 > t1


def test_timer_fires_repeatedly():
    ticks = []
    timer = Timer(0.01, lambda c: ticks.append(c), start_immediately=True)
    timer.start()
    time.sleep(0.05)
    timer.stop()
    assert len(ticks) >= 3


def test_timer_cycle_counter():
    ticks = []
    timer = Timer(0.005, lambda c: ticks.append(c))
    timer.start()
    time.sleep(0.04)
    timer.stop()
    assert timer.cycle == len(ticks) + 1  # 0. döngü atlandı
    assert ticks and ticks[0] == 1


def test_timer_negative_period_raises():
    with pytest.raises(ValueError):
        Timer(-1.0, lambda c: None)


def test_timer_zero_period_raises():
    with pytest.raises(ValueError):
        Timer(0.0, lambda c: None)


def test_timer_running_flag():
    timer = Timer(1.0, lambda c: None)
    assert not timer.running
    timer.start()
    assert timer.running
    timer.stop()
    assert not timer.running


def test_timer_double_start_no_duplicate():
    timer = Timer(1.0, lambda c: None)
    timer.start()
    timer.start()  # ikinci çağrı etkisiz
    timer.stop()


def test_stopwatch_measures():
    sw = Stopwatch()
    sw.start()
    time.sleep(0.01)
    assert sw.elapsed_s() >= 0.009


def test_stopwatch_not_started_zero():
    sw = Stopwatch()
    assert sw.elapsed_ns() == 0


def test_rate_limiter_allows_at_rate():
    limiter = RateLimiter(max_rate_hz=100.0)
    allowed = sum(1 for _ in range(10) if limiter.allow())
    assert allowed == 1  # 10 nanosaniyelik çağrıda yalnızca ilki geçer


def test_rate_limiter_releases_after_wait():
    limiter = RateLimiter(max_rate_hz=50.0)
    assert limiter.allow() is True
    time.sleep(0.03)
    assert limiter.allow() is True


def test_rate_limiter_invalid_rate_raises():
    with pytest.raises(ValueError):
        RateLimiter(0.0)
