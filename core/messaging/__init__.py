"""
TRUSTIA Mesajlaşma Katmanı — Yayın/Abone (Pub-Sub) Altyapısı.

Tasarım ilkeleri:
  * Konu (topic) tabanlı yayın/abone modeli
  * Abonelik filtreleri: konu öneki ve mesaj tipi bazında
  * Bloklamayan yayın: yavaş aboneler sistemi kilitlemez
  * İş parçacığı güvenliği: eşzamanlı yayın/abone güvenlidir
  * Mesaj meta verisi: zaman damgası, kaynak düğüm, sıra numarası
"""

from __future__ import annotations

import threading
import time
import uuid
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, Callable, Dict, List, Optional, Set

from core.errors import TrustiaError


class MessagePriority(IntEnum):
    """Mesaj öncelik seviyeleri — kritik mesajlar sıradan önce işlenir."""

    LOW = 0
    NORMAL = 1
    HIGH = 2
    CRITICAL = 3


@dataclass(frozen=True)
class Header:
    """Her TRUSTIA mesajının taşıdığı ortak meta veri."""

    topic: str
    message_type: str
    node_id: str
    sequence: int
    timestamp_ns: int = field(default_factory=lambda: time.time_ns())
    priority: MessagePriority = MessagePriority.NORMAL
    message_id: str = field(default_factory=lambda: uuid.uuid4().hex)


@dataclass(frozen=True)
class Message:
    """Konu üzerinde taşınan veri sarmalayıcısı."""

    header: Header
    payload: Any

    @classmethod
    def create(
        cls,
        topic: str,
        payload: Any,
        node_id: str,
        sequence: int,
        priority: MessagePriority = MessagePriority.NORMAL,
    ) -> "Message":
        return cls(
            header=Header(
                topic=topic,
                message_type=type(payload).__name__,
                node_id=node_id,
                sequence=sequence,
                priority=priority,
            ),
            payload=payload,
        )


SubscriberFn = Callable[[Message], None]


class Subscription:
    """Bir aboneliği temsil eder; eşleşme kuralı ve geri çağırma içerir."""

    __slots__ = ("subscriber_id", "topic_prefix", "message_type", "callback", "active")

    def __init__(
        self,
        subscriber_id: str,
        topic_prefix: str,
        message_type: Optional[str],
        callback: SubscriberFn,
    ) -> None:
        self.subscriber_id = subscriber_id
        self.topic_prefix = topic_prefix
        self.message_type = message_type
        self.callback = callback
        self.active = True

    def matches(self, message: Message) -> bool:
        """Mesajın bu aboneliğin kurallarına uyup uymadığını döndürür."""
        if not self.active:
            return False
        if not message.header.topic.startswith(self.topic_prefix):
            return False
        if self.message_type is not None:
            if message.header.message_type != self.message_type:
                return False
        return True


class SubscriptionError(TrustiaError):
    """Abonelik işlemlerinde oluşan hatalar."""


class PublishError(TrustiaError):
    """Mesaj yayınında oluşan hatalar."""


class MessageBus:
    """Konu tabanlı, iş parçacığı güvenli yayın/abone mesaj merkezi.

    Örnek kullanım::

        bus = MessageBus()
        bus.subscribe("vehicle/pose", on_pose)

        bus.publish(Message.create("vehicle/pose", pose, node_id="est"))
    """

    def __init__(self, max_queued_per_subscriber: int = 1000) -> None:
        self._lock = threading.RLock()
        self._subscriptions: List[Subscription] = []
        self._queues: Dict[str, List[Message]] = {}
        self._publish_count = 0
        self._dropped_count = 0
        self._max_queued = max_queued_per_subscriber

    def subscribe(
        self,
        topic_prefix: str,
        callback: SubscriberFn,
        message_type: Optional[str] = None,
        subscriber_id: Optional[str] = None,
    ) -> Subscription:
        """Konu öneki ve isteğe bağlı mesaj tipi ile abone olur."""
        with self._lock:
            if subscriber_id is None:
                subscriber_id = f"sub-{uuid.uuid4().hex[:8]}"
            if not topic_prefix:
                raise SubscriptionError("topic_prefix boş olamaz")
            if not callable(callback):
                raise SubscriptionError("callback çağrılabilir bir işlev olmalı")
            subscription = Subscription(
                subscriber_id=subscriber_id,
                topic_prefix=topic_prefix,
                message_type=message_type,
                callback=callback,
            )
            self._subscriptions.append(subscription)
            self._queues[subscriber_id] = []
            return subscription

    def unsubscribe(self, subscription: Subscription) -> bool:
        """Bir aboneliği kaldırır; başarılıysa True döndürür."""
        with self._lock:
            if subscription in self._subscriptions:
                self._subscriptions.remove(subscription)
                self._queues.pop(subscription.subscriber_id, None)
                subscription.active = False
                return True
            subscription.active = False
            return False

    def publish(self, message: Message) -> int:
        """Mesajı tüm uygun abonelere teslim eder.

        Teslim edilen abone sayısını döndürür. Abonelerin geri çağrımları
        sıralı ve engellemesiz işlenir; yavaş abone kuyruğu taşarsa mesaj
        düşürülür ve istatistik güncellenir.
        """
        with self._lock:
            self._publish_count += 1
            delivered = 0
            for subscription in self._subscriptions:
                if subscription.matches(message):
                    queue = self._queues[subscription.subscriber_id]
                    if len(queue) >= self._max_queued:
                        queue.pop(0)
                        self._dropped_count += 1
                    self._enqueue_sorted(queue, message)
                    delivered += 1
            return delivered

    @staticmethod
    def _enqueue_sorted(queue: List[Message], message: Message) -> None:
        """Mesajı öncelik sıralı pozisyona ekler (kritik mesajlar önde)."""
        index = len(queue)
        for i, queued in enumerate(queue):
            if queued.header.priority < message.header.priority:
                index = i
                break
        queue.insert(index, message)

    def deliver_now(self, message: Message) -> int:
        """Mesajı abonelerin kuyruklarına koymadan anında teslim eder.

        Yayın işlemi çağıran iş parçacığını abone hızına bağımlı kılar;
        yalnızca düşük hacimli kritik iletiler için kullanılmalıdır.
        """
        with self._lock:
            self._publish_count += 1
            delivered = 0
            for subscription in self._subscriptions:
                if subscription.matches(message):
                    try:
                        subscription.callback(message)
                        delivered += 1
                    except Exception as exc:  # abone hatası yayını bozmasın
                        self._dropped_count += 1
                        self._record_failure(exc)
            return delivered

    def drain(self, subscriber_id: str, max_messages: int = 64) -> List[Message]:
        """Bir abonenin kuyruğundaki mesajları sırayla alır ve çağırır."""
        with self._lock:
            queue = self._queues.get(subscriber_id)
            if not queue:
                return []
            batch = queue[:max_messages]
            del queue[:max_messages]
        for message in batch:
            try:
                subscription = self._find_active(subscriber_id)
                if subscription is not None:
                    subscription.callback(message)
            except Exception as exc:
                self._record_failure(exc)
        return batch

    def _find_active(self, subscriber_id: str) -> Optional[Subscription]:
        for subscription in self._subscriptions:
            if subscription.subscriber_id == subscriber_id:
                return subscription
        return None

    def _record_failure(self, exc: Exception) -> None:
        """Abone geri çağrım hatalarını sessizce sayar (log katmanı bağlanır)."""

    def statistics(self) -> Dict[str, Any]:
        """Yayın istatistiklerini döndürür."""
        with self._lock:
            return {
                "subscriptions": len(self._subscriptions),
                "published_total": self._publish_count,
                "dropped_total": self._dropped_count,
                "queue_sizes": {
                    sid: len(q) for sid, q in self._queues.items()
                },
            }

    def clear(self) -> None:
        """Tüm abonelikleri ve kuyrukları sıfırlar."""
        with self._lock:
            self._subscriptions.clear()
            self._queues.clear()
            self._dropped_count = 0
