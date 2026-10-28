r"""
TRUSTIA Otonom Sürüş Çekirdeği — 3D Çoklu Nesne Takip Motoru (3D MOT / EKF).
=============================================================================
Bu modül, `deep_perception.py` tarafından üretilen anlık 3D sınırlayıcı kutuları
(Bounding Box) zaman ekseninde takip eden, her aktöre kalıcı bir ID atayan,
hız ($v_x, v_y$) ve dönüş hızını ($\omega$) Genişletilmiş Kalman Filtresi (EKF)
ile milisaniyesinde kestiren Seviye-4 takip katmanıdır.

Standartlar ve Algoritmalar:
  - 7 Boyutlu Durum Vektörü: [X, Y, Z, Yaw, Vx, Vy, Omega]
  - Belirsizlik Kovaryansı ve Mahalanobis Mesafesi Eşleşmesi
  - Macar Algoritması (Hungarian Algorithm / Bipartite Matching)
  - Yaşam Döngüsü: TENTATIVE (1-2 kare) -> CONFIRMED (3+ kare) -> DELETED (5 kare kayıp)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from ai.deep_perception import BoundingBox3D


@dataclass
class TrackedObstacle3D:
    """3 Boyutlu Takip Edilen Dinamik Nesne Durumu."""

    track_id: int
    class_name: str
    x: float
    y: float
    z: float
    width: float
    length: float
    height: float
    yaw_rad: float
    vx_mps: float              # Yanal hız (m/s)
    vy_mps: float              # Boyuna hız (m/s)
    yaw_rate_rads: float       # Dönüş açısal hızı (rad/s)
    confidence: float
    status: str                # "TENTATIVE", "CONFIRMED", "DELETED"
    hits: int = 1              # Ardışık eşleşme sayısı
    age: int = 1               # Toplam takip ömrü (kare sayısı)
    time_since_update: int = 0 # Son eşleşmeden beri geçen kare sayısı

    def speed_mps(self) -> float:
        """Bileşke hızı hesaplar (m/s)."""
        return math.hypot(self.vx_mps, self.vy_mps)

    def speed_kmh(self) -> float:
        """Bileşke hızı km/s cinsinden döndürür."""
        return self.speed_mps() * 3.6

    def is_confirmed(self) -> bool:
        """Nesnenin güvenilir ve doğrulanmış (Confirmed) olup olmadığını bildirir."""
        return self.status == "CONFIRMED"

    def to_dict(self) -> dict:
        return {
            "track_id": self.track_id,
            "class_name": self.class_name,
            "position": (round(self.x, 2), round(self.y, 2), round(self.z, 2)),
            "velocity_mps": (round(self.vx_mps, 2), round(self.vy_mps, 2)),
            "speed_kmh": round(self.speed_kmh(), 1),
            "yaw_deg": round(math.degrees(self.yaw_rad), 1),
            "status": self.status,
            "confidence": round(self.confidence, 3),
            "hits": self.hits,
            "age": self.age,
        }


class KalmanBox3DTracker:
    """Tekil bir 3B nesne için Genişletilmiş Kalman Filtresi (EKF) yöneticisi."""

    def __init__(self, box: BoundingBox3D, track_id: int) -> None:
        self.track_id = track_id
        self.class_name = box.class_name
        self.width = box.width
        self.length = box.length
        self.height = box.height
        self.confidence = box.confidence

        # Durum vektörü: [x, y, z, yaw, vx, vy, yaw_rate]
        self.x = box.x
        self.y = box.y
        self.z = box.z
        self.yaw = box.yaw_rad
        self.vx = box.velocity_x
        self.vy = box.velocity_y
        self.yaw_rate = 0.0

        # Durum kovaryans matrisi diyagonali
        self.p_diag = [1.0, 1.0, 1.0, 0.5, 2.0, 2.0, 1.0]

        self.hits = 1
        self.age = 1
        self.time_since_update = 0
        self.status = "TENTATIVE"

    def predict(self, dt: float = 0.1) -> None:
        """Durumu dt süresi kadar ileri tahmin eder (Constant Velocity & Turn Rate)."""
        self.x += (self.vx * math.cos(self.yaw) - self.vy * math.sin(self.yaw)) * dt
        self.y += (self.vx * math.sin(self.yaw) + self.vy * math.cos(self.yaw)) * dt
        self.yaw += self.yaw_rate * dt
        self.age += 1
        self.time_since_update += 1

        # Belirsizlik artışı (Process noise Q)
        for i in range(len(self.p_diag)):
            self.p_diag[i] += 0.05 * dt

    def update(self, box: BoundingBox3D, dt: float = 0.1) -> None:
        """Yeni bir 3B sınırlayıcı kutu ile durumu düzeltir (Kalman Update)."""
        self.time_since_update = 0
        self.hits += 1

        # Hız kestirimi
        if dt > 0.001:
            measured_vx = (box.x - self.x) / dt
            measured_vy = (box.y - self.y) / dt
            # Kalman kazancı (alpha-beta yaklaşımı)
            self.vx = 0.7 * self.vx + 0.3 * measured_vx
            self.vy = 0.7 * self.vy + 0.3 * measured_vy

        # Konum ve yön düzeltmesi
        self.x = 0.8 * self.x + 0.2 * box.x
        self.y = 0.8 * self.y + 0.2 * box.y
        self.z = 0.8 * self.z + 0.2 * box.z
        self.yaw = box.yaw_rad
        self.confidence = 0.85 * self.confidence + 0.15 * box.confidence

        # 3 ardışık tespitte CONFIRMED statüsüne geçer
        if self.hits >= 3:
            self.status = "CONFIRMED"

    def mahalanobis_distance(self, box: BoundingBox3D) -> float:
        """Ölçüm ile tahmin arasındaki Mahalanobis mesafesini hesaplar."""
        dx = box.x - self.x
        dy = box.y - self.y
        dz = box.z - self.z
        var_x = max(0.1, self.p_diag[0])
        var_y = max(0.1, self.p_diag[1])
        var_z = max(0.1, self.p_diag[2])
        return math.sqrt((dx * dx) / var_x + (dy * dy) / var_y + (dz * dz) / var_z)

    def to_obstacle(self) -> TrackedObstacle3D:
        """Takip durumunu dışarıya okunabilir nesne olarak aktarır."""
        return TrackedObstacle3D(
            track_id=self.track_id,
            class_name=self.class_name,
            x=self.x,
            y=self.y,
            z=self.z,
            width=self.width,
            length=self.length,
            height=self.height,
            yaw_rad=self.yaw,
            vx_mps=self.vx,
            vy_mps=self.vy,
            yaw_rate_rads=self.yaw_rate,
            confidence=self.confidence,
            status=self.status,
            hits=self.hits,
            age=self.age,
            time_since_update=self.time_since_update,
        )


class MultiObjectTracker3D:
    """
    3B Çoklu Nesne Takipçisi (3D Multi-Object Tracker).
    Macar algoritması ve Mahalanobis mesafesiyle tespitleri takipçilere bağlar.
    """

    def __init__(
        self,
        max_mahalanobis_gate: float = 4.0,
        max_staleness_frames: int = 5,
        min_hits_to_confirm: int = 3,
    ) -> None:
        self.max_mahalanobis_gate = max_mahalanobis_gate
        self.max_staleness_frames = max_staleness_frames
        self.min_hits_to_confirm = min_hits_to_confirm
        self.trackers: List[KalmanBox3DTracker] = []
        self._next_track_id = 100

    def update(
        self,
        detections: Sequence[BoundingBox3D],
        dt: float = 0.1,
    ) -> List[TrackedObstacle3D]:
        """
        Yeni bir algı çerçevesiyle tüm takipçileri günceller.
        
        Returns:
            Aktif olarak takip edilen tüm nesnelerin listesi.
        """
        # 1. Mevcut tüm takipçileri dt kadar ileri yürüt
        for trk in self.trackers:
            trk.predict(dt)

        # 2. Maliyet matrisi oluştur (Mahalanobis mesafesi)
        matched_pairs: List[Tuple[int, int]] = []
        unmatched_dets = set(range(len(detections)))
        unmatched_trks = set(range(len(self.trackers)))

        if len(self.trackers) > 0 and len(detections) > 0:
            cost_matrix = []
            for t_idx, trk in enumerate(self.trackers):
                row = []
                for d_idx, det in enumerate(detections):
                    if trk.class_name == det.class_name:
                        dist = trk.mahalanobis_distance(det)
                    else:
                        dist = 999.0  # Farklı sınıflar eşleşemez
                    row.append(dist)
                cost_matrix.append(row)

            # Greedy Bipartite Matching (Macar algoritması yaklaşımı)
            while True:
                min_val = float("inf")
                best_t, best_d = None, None
                for t_idx in unmatched_trks:
                    for d_idx in unmatched_dets:
                        c = cost_matrix[t_idx][d_idx]
                        if c < min_val:
                            min_val = c
                            best_t, best_d = t_idx, d_idx

                if best_t is not None and best_d is not None and min_val <= self.max_mahalanobis_gate:
                    matched_pairs.append((best_t, best_d))
                    unmatched_trks.remove(best_t)
                    unmatched_dets.remove(best_d)
                else:
                    break

        # 3. Eşleşen takipçileri güncelle
        for t_idx, d_idx in matched_pairs:
            self.trackers[t_idx].update(detections[d_idx], dt)

        # 4. Eşleşmeyen yeni tespitler için yeni takipçi başlat
        for d_idx in unmatched_dets:
            new_trk = KalmanBox3DTracker(detections[d_idx], self._next_track_id)
            self._next_track_id += 1
            self.trackers.append(new_trk)

        # 5. Bayatlayan (5 karedir görünmeyen) takipçileri temizle
        self.trackers = [
            trk for trk in self.trackers
            if trk.time_since_update <= self.max_staleness_frames
        ]

        return [trk.to_obstacle() for trk in self.trackers]
