"""Sistem 6 — Koordinat dönüşümleri birim testleri.

Referans değerler: WGS84 elipsoidi üzerinde kararlı ve bilinen
koordinatlar. Ankara Kızılay için UTM 36S bölgesi kullanılır.
Doğruluk toleransı: konum ~1 cm, mesafe ~0.1 m.
"""

import math

import pytest

from core.errors import NavigationError
from core.transforms import (
    GeoPoint,
    UtmPoint,
    EnuPoint,
    LocalFrame,
    geodetic_to_utm,
    geodetic_to_utm_zone,
    utm_to_geodetic,
    haversine_distance,
)

# Ankara Kızılay (bilinen referans)
ANKARA = GeoPoint(latitude_deg=39.92077, longitude_deg=32.85411)
ANKARA_UTM = geodetic_to_utm(ANKARA)

# Bilinen mutlak UTM noktaları (Ankara bölgesi, bölge 36S)
REF_UTM = UtmPoint(
    easting_m=500000.0,
    northing_m=4419000.0,
    zone=36,
    hemisphere="N",
)
REF_GEO = utm_to_geodetic(REF_UTM)


def test_ankara_utm_zone():
    assert ANKARA_UTM.zone == 36
    assert ANKARA_UTM.hemisphere == "N"


def test_roundtrip_geodetic_utm():
    back = utm_to_geodetic(ANKARA_UTM)
    assert abs(back.latitude_deg - ANKARA.latitude_deg) < 1e-7
    assert abs(back.longitude_deg - ANKARA.longitude_deg) < 1e-7


def test_reference_utm_roundtrip():
    back = utm_to_geodetic(REF_UTM)
    forth = geodetic_to_utm_zone(back, REF_UTM.zone, REF_UTM.hemisphere)
    assert abs(forth.easting_m - REF_UTM.easting_m) < 0.01
    assert abs(forth.northing_m - REF_UTM.northing_m) < 0.01


def test_local_frame_origin_zero():
    frame = LocalFrame(ANKARA)
    local = frame.to_local(ANKARA)
    assert abs(local.east_m) < 0.01
    assert abs(local.north_m) < 0.01


def test_local_frame_roundtrip():
    frame = LocalFrame(ANKARA)
    target = GeoPoint(39.93, 32.87)
    local = frame.to_local(target)
    back = frame.from_local(local)
    assert abs(back.latitude_deg - target.latitude_deg) < 1e-9
    assert abs(back.longitude_deg - target.longitude_deg) < 1e-9
    assert local.east_m > 0
    assert local.north_m > 0


def test_local_distance_matches_haversine():
    frame = LocalFrame(ANKARA)
    far = GeoPoint(40.0, 33.0)
    local = frame.to_local(far)
    distance = math.hypot(local.east_m, local.north_m)
    hav = haversine_distance(ANKARA, far)
    # UTM konformal projeksiyon distorsiyonu ~%0.03 → 15 km'de ~5 m sapma normal
    assert abs(distance - hav) < 10.0


def test_haversine_known_distance():
    # Ekvatorda 1 derece boylam ~111.32 km
    a = GeoPoint(0.0, 0.0)
    b = GeoPoint(0.0, 1.0)
    dist = haversine_distance(a, b)
    assert abs(dist - 111320.0) < 1000.0


def test_haversine_zero():
    assert haversine_distance(ANKARA, ANKARA) == 0.0


def test_invalid_latitude_raises():
    with pytest.raises(NavigationError):
        GeoPoint(91.0, 0.0).validate()


def test_invalid_longitude_raises():
    with pytest.raises(NavigationError):
        GeoPoint(0.0, 181.0).validate()


def test_invalid_utm_zone_raises():
    with pytest.raises(NavigationError):
        geodetic_to_utm_zone(ANKARA, 0, "N")


def test_invalid_hemisphere_raises():
    with pytest.raises(NavigationError):
        geodetic_to_utm_zone(ANKARA, 36, "X")


def test_enu_distance_and_operators():
    a = EnuPoint(0.0, 0.0)
    b = EnuPoint(3.0, 4.0)
    assert abs(a.distance_to(b) - 5.0) < 1e-9
    diff = b - a
    assert diff.east_m == 3.0
    total = a + b
    assert total.north_m == 4.0


def test_zone_boundary_switch():
    # 35. bölge sonu (30°E sınırı) / 36. bölge başı
    west = GeoPoint(39.0, 29.999999)
    east = GeoPoint(39.0, 30.000001)
    assert geodetic_to_utm(west).zone == 35
    assert geodetic_to_utm(east).zone == 36


def test_southern_hemisphere_zone():
    santiago = GeoPoint(-33.4489, -70.6693)  # Santiago, Şili
    utm = geodetic_to_utm(santiago)
    assert utm.hemisphere == "S"
    back = utm_to_geodetic(utm)
    assert abs(back.latitude_deg - santiago.latitude_deg) < 1e-6
    assert abs(back.longitude_deg - santiago.longitude_deg) < 1e-6
