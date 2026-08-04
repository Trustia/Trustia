"""
TRUSTIA Koordinat Dönüşümleri — WGS84, UTM ve ENU çerçeveleri.

Bu modül, araç konumunu küresel (WGS84 enlem/boylam) ile yerel
(ENU metre) çerçeveler arasında taşır. UTM dönüşümleri, WGS84
elipsoidi (WGS84) üzerinde Karney (2003) serisini uygular.

Dönüşümler bağımsız ve tekrar üretilebilir; birim testlerde
yüksek doğruluklu referans noktalarıyla doğrulanır.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from core.errors import NavigationError

_WGS84_A = 6378137.0
_WGS84_F = 1.0 / 298.257223563
_WGS84_B = _WGS84_A * (1.0 - _WGS84_F)
_WGS84_E2 = _WGS84_F * (2.0 - _WGS84_F)
_WGS84_EP2 = _WGS84_E2 / (1.0 - _WGS84_E2)


@dataclass(frozen=True)
class GeoPoint:
    """WGS84 koordinatı — derece cinsinden enlem ve boylam."""

    latitude_deg: float
    longitude_deg: float
    altitude_m: float = 0.0

    def validate(self) -> None:
        if not -90.0 <= self.latitude_deg <= 90.0:
            raise NavigationError(f"enlem aralık dışı: {self.latitude_deg}")
        if not -180.0 <= self.longitude_deg <= 180.0:
            raise NavigationError(f"boylam aralık dışı: {self.longitude_deg}")


@dataclass(frozen=True)
class UtmPoint:
    """UTM koordinatı — metre cinsinden doğu/kuzey + bölge."""

    easting_m: float
    northing_m: float
    zone: int
    hemisphere: str  # "N" veya "S"
    altitude_m: float = 0.0


@dataclass(frozen=True)
class EnuPoint:
    """Yerel ENU (Doğu-Kuzey-Yukarı) koordinatı — metre."""

    east_m: float
    north_m: float
    up_m: float = 0.0

    def distance_to(self, other: "EnuPoint") -> float:
        de = self.east_m - other.east_m
        dn = self.north_m - other.north_m
        du = self.up_m - other.up_m
        return math.sqrt(de * de + dn * dn + du * du)

    def __add__(self, other: "EnuPoint") -> "EnuPoint":
        return EnuPoint(
            self.east_m + other.east_m,
            self.north_m + other.north_m,
            self.up_m + other.up_m,
        )

    def __sub__(self, other: "EnuPoint") -> "EnuPoint":
        return EnuPoint(
            self.east_m - other.east_m,
            self.north_m - other.north_m,
            self.up_m - other.up_m,
        )


def _zone_number(longitude_deg: float) -> int:
    return int((longitude_deg + 180.0) // 6) + 1


def _central_meridian(zone: int) -> float:
    return (zone - 1) * 6.0 - 180.0 + 3.0


def _to_utm_zone(zone: int, hemisphere: str) -> None:
    if not 1 <= zone <= 60:
        raise NavigationError(f"UTM bölgesi aralık dışı: {zone}")
    if hemisphere not in ("N", "S"):
        raise NavigationError(f"hemisfer geçersiz: {hemisphere!r}")


def geodetic_to_utm(point: GeoPoint) -> UtmPoint:
    """WGS84 derece koordinatını UTM metre koordinatına çevirir."""
    point.validate()
    zone = _zone_number(point.longitude_deg)
    hemisphere = "N" if point.latitude_deg >= 0.0 else "S"
    return geodetic_to_utm_zone(point, zone, hemisphere)


def geodetic_to_utm_zone(
    point: GeoPoint, zone: int, hemisphere: str
) -> UtmPoint:
    """Belirtilen UTM bölgesine dönüşüm (sınır bölgeleri için)."""
    point.validate()
    _to_utm_zone(zone, hemisphere)

    lat = math.radians(point.latitude_deg)
    lon = math.radians(point.longitude_deg)
    lon0 = math.radians(_central_meridian(zone))

    N = _WGS84_A / math.sqrt(1.0 - _WGS84_E2 * math.sin(lat) ** 2)
    T = math.tan(lat) ** 2
    C = _WGS84_EP2 * math.cos(lat) ** 2
    A = math.cos(lat) * (lon - lon0)

    M = _WGS84_A * (
        (1.0 - _WGS84_E2 / 4.0 - 3.0 * _WGS84_E2**2 / 64.0
         - 5.0 * _WGS84_E2**3 / 256.0) * lat
        - (3.0 * _WGS84_E2 / 8.0 + 3.0 * _WGS84_E2**2 / 32.0
           + 45.0 * _WGS84_E2**3 / 1024.0) * math.sin(2.0 * lat)
        + (15.0 * _WGS84_E2**2 / 256.0
           + 45.0 * _WGS84_E2**3 / 1024.0) * math.sin(4.0 * lat)
        - (35.0 * _WGS84_E2**3 / 3072.0) * math.sin(6.0 * lat)
    )

    M0 = 0.0  # ekvator

    k0 = 0.9996
    e1 = (1.0 - math.sqrt(1.0 - _WGS84_E2)) / (1.0 + math.sqrt(1.0 - _WGS84_E2))

    x = k0 * N * (
        A
        + (1.0 - T + C) * A**3 / 6.0
        + (5.0 - 18.0 * T + T**2 + 72.0 * C - 58.0 * _WGS84_EP2) * A**5 / 120.0
    )
    y = k0 * (
        (M - M0)
        + N * math.tan(lat)
        * (
            A**2 / 2.0
            + (5.0 - T + 9.0 * C + 4.0 * C**2) * A**4 / 24.0
            + (61.0 - 58.0 * T + T**2 + 600.0 * C - 330.0 * _WGS84_EP2)
            * A**6 / 720.0
        )
    )

    easting = x + 500000.0
    northing = y if hemisphere == "N" else y + 10000000.0
    return UtmPoint(
        easting_m=easting,
        northing_m=northing,
        zone=zone,
        hemisphere=hemisphere,
        altitude_m=point.altitude_m,
    )


def utm_to_geodetic(utm: UtmPoint) -> GeoPoint:
    """UTM metre koordinatını WGS84 derece koordinatına çevirir."""
    _to_utm_zone(utm.zone, utm.hemisphere)

    k0 = 0.9996
    x = utm.easting_m - 500000.0
    y = utm.northing_m if utm.hemisphere == "N" else utm.northing_m - 10000000.0

    lon0 = math.radians(_central_meridian(utm.zone))

    e1 = (1.0 - math.sqrt(1.0 - _WGS84_E2)) / (1.0 + math.sqrt(1.0 - _WGS84_E2))
    M = y / k0
    mu = M / (_WGS84_A * (1.0 - _WGS84_E2 / 4.0 - 3.0 * _WGS84_E2**2 / 64.0
                          - 5.0 * _WGS84_E2**3 / 256.0))

    phi1 = mu + (
        (3.0 * e1 / 2.0 - 27.0 * e1**3 / 32.0) * math.sin(2.0 * mu)
        + (21.0 * e1**2 / 16.0 - 55.0 * e1**4 / 32.0) * math.sin(4.0 * mu)
        + (151.0 * e1**3 / 96.0) * math.sin(6.0 * mu)
        + (1097.0 * e1**4 / 512.0) * math.sin(8.0 * mu)
    )

    N1 = _WGS84_A / math.sqrt(1.0 - _WGS84_E2 * math.sin(phi1) ** 2)
    T1 = math.tan(phi1) ** 2
    C1 = _WGS84_EP2 * math.cos(phi1) ** 2
    R1 = (_WGS84_A * (1.0 - _WGS84_E2)
          / (1.0 - _WGS84_E2 * math.sin(phi1) ** 2) ** 1.5)
    D = x / (N1 * k0)

    lat = phi1 - (N1 * math.tan(phi1) / R1) * (
        D**2 / 2.0
        - (5.0 + 3.0 * T1 + 10.0 * C1 - 4.0 * C1**2 - 9.0 * _WGS84_EP2)
        * D**4 / 24.0
        + (61.0 + 90.0 * T1 + 298.0 * C1 + 45.0 * T1**2
           - 252.0 * _WGS84_EP2 - 3.0 * C1**2)
        * D**6 / 720.0
    )
    lon = lon0 + (
        D
        - (1.0 + 2.0 * T1 + C1) * D**3 / 6.0
        + (5.0 - 2.0 * C1 + 28.0 * T1 - 3.0 * C1**2 + 8.0 * _WGS84_EP2
           + 24.0 * T1**2) * D**5 / 120.0
    ) / math.cos(phi1)

    return GeoPoint(
        latitude_deg=math.degrees(lat),
        longitude_deg=math.degrees(lon),
        altitude_m=utm.altitude_m,
    )


class LocalFrame:
    """Sabit bir orijine göre ENU yerel çerçevesi.

    Orijin WGS84 koordinatıyla tanımlanır; tüm araç konumları bu
    orijine göre metre cinsinden ifade edilir. GPS'siz görevlerde
    görev başlangıç noktası orijin alınır.
    """

    def __init__(self, origin: GeoPoint) -> None:
        origin.validate()
        self._origin = origin

    @property
    def origin(self) -> GeoPoint:
        return self._origin

    def to_local(self, point: GeoPoint) -> EnuPoint:
        """Küresel koordinatı yerel metreye çevirir."""
        point.validate()
        utm_origin = geodetic_to_utm(self._origin)
        utm_point = geodetic_to_utm_zone(
            point, utm_origin.zone, utm_origin.hemisphere
        )
        return EnuPoint(
            east_m=utm_point.easting_m - utm_origin.easting_m,
            north_m=utm_point.northing_m - utm_origin.northing_m,
            up_m=utm_point.altitude_m - utm_origin.altitude_m,
        )

    def from_local(self, local: EnuPoint) -> GeoPoint:
        """Yerel metreyi küresel koordinata çevirir."""
        utm_origin = geodetic_to_utm(self._origin)
        utm_point = UtmPoint(
            easting_m=utm_origin.easting_m + local.east_m,
            northing_m=utm_origin.northing_m + local.north_m,
            zone=utm_origin.zone,
            hemisphere=utm_origin.hemisphere,
            altitude_m=utm_origin.altitude_m + local.up_m,
        )
        return utm_to_geodetic(utm_point)


def haversine_distance(a: GeoPoint, b: GeoPoint) -> float:
    """İki küresel nokta arası büyük daire mesafesi (metre)."""
    a.validate()
    b.validate()
    lat1, lon1 = math.radians(a.latitude_deg), math.radians(a.longitude_deg)
    lat2, lon2 = math.radians(b.latitude_deg), math.radians(b.longitude_deg)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = (math.sin(dlat / 2.0) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2)
    return 2.0 * _WGS84_A * math.asin(math.sqrt(h))
