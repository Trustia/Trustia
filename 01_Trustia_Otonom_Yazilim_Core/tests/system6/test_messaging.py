"""Sistem 6 — MessageBus birim testleri."""

import threading

import pytest

from core.messaging import (
    MessageBus,
    Message,
    Header,
    Subscription,
    MessagePriority,
    SubscriptionError,
)


def make_bus() -> MessageBus:
    return MessageBus()


def msg(topic, payload=None, priority=MessagePriority.NORMAL):
    return Message.create(
        topic=topic,
        payload=payload if payload is not None else {},
        node_id="tester",
        sequence=0,
        priority=priority,
    )


def drain_all(bus, subscription) -> list:
    return bus.drain(subscription.subscriber_id, max_messages=10000)


def test_publish_deliver_flow():
    bus = make_bus()
    received = []
    sub = bus.subscribe("topic.test", received.append)
    bus.publish(msg("topic.test", {"value": 42}))
    batch = drain_all(bus, sub)
    assert len(batch) == 1
    assert received[0].payload["value"] == 42


def test_subscription_filter_by_topic_prefix():
    bus = make_bus()
    received = []
    sub = bus.subscribe("topic.a", received.append)
    bus.publish(msg("topic.b"))
    bus.publish(msg("topic.a"))
    assert len(drain_all(bus, sub)) == 1


def test_multiple_subscribers_all_receive():
    bus = make_bus()
    a, b = [], []
    sub_a = bus.subscribe("t", a.append)
    sub_b = bus.subscribe("t", b.append)
    bus.publish(msg("t"))
    drain_all(bus, sub_a)
    drain_all(bus, sub_b)
    assert a and b


def test_unsubscribe_stops_delivery():
    bus = make_bus()
    received = []
    sub = bus.subscribe("t", received.append)
    bus.publish(msg("t"))
    assert bus.unsubscribe(sub) is True
    assert drain_all(bus, sub) == []
    assert received == []


def test_unsubscribe_foreign_handle_returns_false():
    bus = make_bus()
    assert bus.unsubscribe(Subscription("yok", "t", None, lambda m: None)) is False


def test_subscribe_empty_prefix_raises():
    bus = make_bus()
    with pytest.raises(SubscriptionError):
        bus.subscribe("", lambda m: None)


def test_subscribe_non_callable_raises():
    bus = make_bus()
    with pytest.raises(SubscriptionError):
        bus.subscribe("t", "callable-değil")


def test_priority_ordering_high_first_in_queue():
    bus = make_bus()
    received = []
    sub = bus.subscribe("t", received.append)
    for priority in (
        MessagePriority.LOW,
        MessagePriority.HIGH,
        MessagePriority.CRITICAL,
        MessagePriority.NORMAL,
    ):
        bus.publish(msg("t", priority=priority))
    drain_all(bus, sub)
    assert [m.header.priority.name for m in received] == [
        "CRITICAL",
        "HIGH",
        "NORMAL",
        "LOW",
    ]


def test_deliver_now_calls_immediately():
    bus = make_bus()
    received = []
    bus.subscribe("t", received.append)
    bus.deliver_now(msg("t"))
    assert len(received) == 1


def test_statistics_counts():
    bus = make_bus()
    received = []
    sub = bus.subscribe("t", received.append)
    for _ in range(5):
        bus.publish(msg("t"))
    drain_all(bus, sub)
    stats = bus.statistics()
    assert stats["published_total"] == 5
    assert stats["subscriptions"] == 1
    assert stats["queue_sizes"][sub.subscriber_id] == 0


def test_thread_safety_burst():
    bus = make_bus()
    received = []
    received_lock = threading.Lock()
    def append(message):
        with received_lock:
            received.append(message)
    sub = bus.subscribe("burst", append)
    barrier = threading.Barrier(8)

    def worker():
        barrier.wait()
        for _ in range(50):
            bus.publish(msg("burst"))

    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=10)

    drain_all(bus, sub)
    assert len(received) == 400


def test_message_header_defaults():
    message = msg("t")
    assert message.header.topic == "t"
    assert message.header.node_id == "tester"
    assert message.header.priority == MessagePriority.NORMAL
    assert message.header.sequence == 0
    assert message.header.timestamp_ns > 0
    assert message.header.message_id


def test_message_type_inferred_from_payload():
    message = msg("t", payload={"a": 1})
    assert message.header.message_type == "dict"


def test_drain_limited_batch():
    bus = make_bus()
    received = []
    sub = bus.subscribe("t", received.append)
    for _ in range(10):
        bus.publish(msg("t"))
    batch = bus.drain(sub.subscriber_id, max_messages=4)
    assert len(batch) == 4
    assert len(received) == 4
    assert bus.statistics()["queue_sizes"][sub.subscriber_id] == 6


def test_queue_overflow_drops_oldest():
    bus = MessageBus(max_queued_per_subscriber=3)
    received = []
    sub = bus.subscribe("t", received.append)
    for _ in range(5):
        bus.publish(msg("t"))
    stats = bus.statistics()
    assert stats["queue_sizes"][sub.subscriber_id] == 3
    assert stats["dropped_total"] == 2
