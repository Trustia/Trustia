"""
TRUSTIA Simülasyon Dünyası — Arazi üretici ve hava motoru.

PLAN.md 3.4 gereksinimleri (çekirdek alt küme):
  * Prosedürel arazi: engel üretimi, yasak bölgeler, geçilmezlik
  * Hava motoru: yağmur (sensör gürültüsü), sis (menzil azalması),
    gece (görüş kısıtı) — deterministik seed ile
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class TerrainObstacle:
    """Arazideki tek engel (çember modeli)."""

    x_m: float
    y_m: float
    radius_m: float
    kind: str = "kaya"  # kaya / duvar / çamur / su

    def contains(self, x: float, y: float) -> bool:
        return math.hypot(x - self.x_m, y - self.y_m) <= self.radius_m


@dataclass(frozen=True)
class ForbiddenZone:
    """Görev yasak bölgesi (çember)."""

    x_m: float
    y_m: float
    radius_m: float


class Terrain:
    """2D prosedürel arazi — çember engelleri ve yasak bölgeler.

    Engeller deterministik üretilir (seed); başlangıç/hedef
    bölgeleri engellerden arındırılır.
    """

    def __init__(
        self,
        width_m: float = 50.0,
        height_m: float = 50.0,
        seed: int = 0,
        obstacle_count: int = 0,
        obstacle_min_r: float = 0.5,
        obstacle_max_r: float = 2.0,
        forbidden_count: int = 0,
    ) -> None:
        if width_m <= 0.0 or height_m <= 0.0:
            raise ValueError("arazi boyutları pozitif olmalı")
        if obstacle_count < 0 or forbidden_count < 0:
            raise ValueError("sayılar negatif olamaz")
        self._width = width_m
        self._height = height_m
        self._seed = seed
        self._obstacles: List[TerrainObstacle] = []
        self._forbidden: List[ForbiddenZone] = []
        rng = random.Random(seed)
        for _ in range(obstacle_count):
            radius = rng.uniform(obstacle_min_r, obstacle_max_r)
            x = rng.uniform(radius, width_m - radius)
            y = rng.uniform(radius, height_m - radius)
            self._obstacles.append(
                TerrainObstacle(x_m=x, y_m=y, radius_m=radius)
            )
        for _ in range(forbidden_count):
            self._forbidden.append(ForbiddenZone(
                x_m=rng.uniform(2.0, width_m - 2.0),
                y_m=rng.uniform(2.0, height_m - 2.0),
                radius_m=rng.uniform(1.5, 4.0),
            ))
        self._hazards: List = list(self._obstacles) + list(self._forbidden)

    @property
    def width_m(self) -> float:
        return self._width

    @property
    def height_m(self) -> float:
        return self._height

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def obstacles(self) -> List[TerrainObstacle]:
        return list(self._obstacles)

    def add_obstacle(self, x_m: float, y_m: float, radius_m: float) -> None:
        """Çalışma zamanı engel ekler; algı (raycast) listesine de yazar."""
        if radius_m < 0.0:
            raise ValueError("engel yarıçapı negatif olamaz")
        obstacle = TerrainObstacle(x_m=x_m, y_m=y_m, radius_m=radius_m)
        self._obstacles.append(obstacle)
        self._hazards.append(obstacle)

    @property
    def forbidden(self) -> List[ForbiddenZone]:
        return list(self._forbidden)

    def add_forbidden(self, x_m: float, y_m: float, radius_m: float) -> None:
        """Yasak bölge ekler; algı (raycast) listesine de yazar."""
        if radius_m < 0.0:
            raise ValueError("yasak bölge yarıçapı negatif olamaz")
        zone = ForbiddenZone(x_m=x_m, y_m=y_m, radius_m=radius_m)
        self._forbidden.append(zone)
        self._hazards.append(zone)

    def is_blocked(self, x: float, y: float, clearance_m: float = 0.0) -> bool:
        """Nokta engel içinde mi (güvenlik payıyla)."""
        for obstacle in self._obstacles:
            effective = obstacle.radius_m + clearance_m
            if math.hypot(x - obstacle.x_m, y - obstacle.y_m) <= effective:
                return True
        return False

    def in_forbidden(self, x: float, y: float) -> bool:
        for zone in self._forbidden:
            if math.hypot(x - zone.x_m, y - zone.y_m) <= zone.radius_m:
                return True
        return False

    def sample_clear_point(
        self, rng: random.Random, clearance_m: float = 2.0
    ) -> Tuple[float, float]:
        """Engel ve yasak bölgelerden arınmış nokta üretir (en fazla 500 deneme)."""
        for _ in range(500):
            x = rng.uniform(1.0, self._width - 1.0)
            y = rng.uniform(1.0, self._height - 1.0)
            if not self.is_blocked(x, y, clearance_m):
                forbidden_dist, _, _ = self.nearest_forbidden(x, y)
                if forbidden_dist >= clearance_m:
                    return x, y
        raise ValueError("boş nokta bulunamadı")

    def raycast(
        self,
        origin: Tuple[float, float],
        direction_rad: float,
        max_range_m: float,
    ) -> float:
        """Işının ilk çarpışmaya kadar mesafesi (engel + yasak bölge + sınır).

        Hiç çarpışma yoksa max_range_m döner. Yasak bölgeler sanal
        engel olarak işlenir (geçilmez çember); dünya sınırı da
        sanal duvar olarak algılanır.
        """
        ox, oy = origin
        cos_a, sin_a = math.cos(direction_rad), math.sin(direction_rad)
        closest = max_range_m
        hazards = self._hazards
        for hazard in hazards:
            dx = hazard.x_m - ox
            dy = hazard.y_m - oy
            d2 = dx * dx + dy * dy
            r = hazard.radius_m
            reach = closest + r
            if d2 > reach * reach:
                continue  # mevcut en yakından uzak — ışın kesinlikle ıskalar
            proj = dx * cos_a + dy * sin_a
            if proj <= 0.0:
                continue  # ışının gerisinde
            perp_sq = d2 - proj * proj
            if perp_sq > r * r:
                continue  # ışın engeli ıskalar
            along = proj - math.sqrt(r * r - perp_sq)
            if along < closest:
                closest = along
        boundary = self._boundary_distance(ox, oy, cos_a, sin_a)
        if boundary is not None and boundary < closest:
            closest = boundary
        return closest

    def _boundary_distance(
        self,
        ox: float,
        oy: float,
        cos_a: float,
        sin_a: float,
    ) -> Optional[float]:
        """Işın-dikdörtgen (sanal duvar) çıkış mesafesi; sınır yoksa None."""
        width, height = self._width, self._height
        tmin = 0.0
        tmax = math.inf
        if abs(cos_a) < 1e-12:
            if not (0.0 <= ox <= width):
                return None
        else:
            t1 = (0.0 - ox) / cos_a
            t2 = (width - ox) / cos_a
            if t1 > t2:
                t1, t2 = t2, t1
            tmin = max(tmin, t1)
            tmax = min(tmax, t2)
        if abs(sin_a) < 1e-12:
            if not (0.0 <= oy <= height):
                return None
        else:
            t1 = (0.0 - oy) / sin_a
            t2 = (height - oy) / sin_a
            if t1 > t2:
                t1, t2 = t2, t1
            tmin = max(tmin, t1)
            tmax = min(tmax, t2)
        if tmax < tmin:
            return None
        if tmin > 1e-12:
            return tmin  # ışın dışarıda başlar — giriş mesafesi
        return tmax  # içeride başlar — çıkış mesafesi

    def nearest_obstacle_distance(self, x: float, y: float) -> float:
        """Noktaya en yakın engel yüzeyine mesafe (negatif: içinde)."""
        best = math.inf
        for obstacle in self._obstacles:
            distance = math.hypot(x - obstacle.x_m, y - obstacle.y_m)
            best = min(best, distance - obstacle.radius_m)
        return best if math.isfinite(best) else math.inf

    def nearest_forbidden(
        self, x: float, y: float
    ) -> Tuple[float, float, float]:
        """En yakın yasak bölgeye (yüzey mesafesi, merkez_x, merkez_y).

        Mesafe yüzeye kadardır; bölge içinde negatif döner.
        """
        best_dist = math.inf
        best_x = 0.0
        best_y = 0.0
        for zone in self._forbidden:
            center_dist = math.hypot(x - zone.x_m, y - zone.y_m)
            surface_dist = center_dist - zone.radius_m
            if surface_dist < best_dist:
                best_dist = surface_dist
                best_x = zone.x_m
                best_y = zone.y_m
        if not math.isfinite(best_dist):
            return (math.inf, 0.0, 0.0)
        return (best_dist, best_x, best_y)


class Weather:
    """Hava durumu motoru — sensör etkilerini yapılandırır.

    Etkiler (PLAN 3.4):
      * yağmur_mmh : LiDAR gürültüsünü artırır
      * sis_density (0-1) : LiDAR menzilini azaltır
      * gece (bool) : gündüz/gece kısıtını simüle eder (metrik kaydı)
    """

    def __init__(
        self,
        rain_mmh: float = 0.0,
        fog_density: float = 0.0,
        night: bool = False,
    ) -> None:
        if rain_mmh < 0.0:
            raise ValueError("yağmur negatif olamaz")
        if not 0.0 <= fog_density <= 1.0:
            raise ValueError("sis yoğunluğu 0-1 aralığında olmalı")
        self._rain = rain_mmh
        self._fog = fog_density
        self._night = night

    @property
    def rain_mmh(self) -> float:
        return self._rain

    @property
    def fog_density(self) -> float:
        return self._fog

    @property
    def night(self) -> bool:
        return self._night

    def lidar_range_factor(self) -> float:
        """Sis nedeniyle görüş menzili çarpanı (1.0 temiz hava)."""
        return 1.0 - 0.8 * self._fog

    def lidar_noise_sigma_m(self, base_sigma_m: float) -> float:
        """Yağmur + sis nedeniyle gürültü standart sapması."""
        return base_sigma_m * (1.0 + 0.15 * self._rain + 0.1 * self._fog)

    def odometry_noise_factor(self) -> float:
        """Islak zemin nedeniyle odometri kayması çarpanı."""
        return 1.0 + 0.05 * self._rain

    def describe(self) -> str:
        parts = []
        if self._rain > 0.0:
            parts.append(f"yağmur {self._rain:.0f} mm/h")
        if self._fog > 0.0:
            parts.append(f"sis %{self._fog * 100.0:.0f}")
        if self._night:
            parts.append("gece")
        return ", ".join(parts) if parts else "temiz hava"


@dataclass
class TerrainSpec:
    """Arazi üretim parametreleri — senaryo üreticisinin çıktısı."""

    width_m: float
    height_m: float
    seed: int
    obstacle_count: int
    forbidden_count: int
    obstacle_min_r: float = 0.5
    obstacle_max_r: float = 2.0
