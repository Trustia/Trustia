"""
TRUSTIA Robotaksi Yolcu Kabin Güvenliği, Kapı Kilidi (Door Interlock) ve EV Batarya/Termal Yöneticisi
====================================================================================================
Sürücüsüz bir ticari Robotakside (SAIC Maxus MIFA 7 / Hyundai Ioniq 5) yolcu güvenliği ve elektrikli
araç batarya sağlığı için zorunlu olan denetimleri yürütür:
  1. Kapı Emniyet Kilidi (Door Interlock): Herhangi bir kapı veya bagaj tam kapanmamışsa aracın
     kalkışını kilitler (HOLD_BRAKE_INTERLOCK).
  2. Emniyet Kemeri ve Yolcu Oturma Algılama: Yolcu koltukta oturuyor ancak kemeri takılı değilse
     sesli/görsel uyarı verir ve kalkışı bekletir.
  3. Yolcu Acil Durdurma / Sağa Çekme Butonu (Cabin SOS / Pullover Button): Yolcu kabin içi acil
     durdurma butonuna bastığında 1.5 m/s² kontrollü sağa çekme (MRM) başlatır ve çağrı merkezini bağlar.
  4. Yüksek Voltaj Batarya (BMS) ve Termal Yönetim: Şarj seviyesi (SoC) %18'in altına düştüğünde
     yeni yolcu alımını kapatıp şarj istasyonuna yönlendirir; batarya sıcaklığı > 48°C ise güç sınırlar.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CabinDoorSeatStatus:
    """Robotaksi kabin kapı, emniyet kemeri ve yolcu acil buton durumu."""

    all_doors_closed: bool
    trunk_closed: bool
    passenger_seated: bool
    seatbelt_fastened: bool
    passenger_sos_pressed: bool = False


@dataclass(frozen=True)
class BatteryThermalState:
    """Elektrikli Robotaksi (90 kWh / 77.4 kWh) batarya ve termal durumu."""

    soc_percent: float
    pack_temp_c: float
    estimated_range_km: float


@dataclass(frozen=True)
class CabinSafetyDecision:
    """Kabin güvenliği ve batarya yöneticisinin ürettiği operasyonel karar."""

    dispatch_allowed: bool
    motion_inhibit_brake_hold: bool
    trigger_passenger_mrm: bool
    intercom_call_center_active: bool
    fleet_state_recommendation: str  # "READY_FOR_PASSENGER", "IN_RIDE", "HOLD_DOOR_OR_BELT", "PASSENGER_SOS_MRM", "RETURN_TO_CHARGER"
    max_power_derating_ratio: float
    reason: str


class RobotaxiCabinAndBmsSupervisor:
    """
    Ticari Robotaksi yolcu kabin emniyeti (kapı kilidi, kemer, SOS butonu) ve
    elektrikli araç BMS batarya/termal koruma yöneticisi.
    """

    def __init__(
        self,
        min_dispatch_soc_percent: float = 18.0,
        thermal_derate_temp_c: float = 48.0,
    ) -> None:
        self.min_dispatch_soc_percent = min_dispatch_soc_percent
        self.thermal_derate_temp_c = thermal_derate_temp_c

    def evaluate(
        self,
        cabin: CabinDoorSeatStatus,
        bms: BatteryThermalState,
        vehicle_speed_mps: float,
    ) -> CabinSafetyDecision:
        """Kabin ve batarya durumunu değerlendirerek güvenli hareket izni üretir."""
        # 1. Yolcu kabin içi SOS / Acil Sağa Çekme butonuna bastıysa
        if cabin.passenger_sos_pressed:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=(vehicle_speed_mps < 0.2),
                trigger_passenger_mrm=True,
                intercom_call_center_active=True,
                fleet_state_recommendation="PASSENGER_SOS_MRM",
                max_power_derating_ratio=0.5,
                reason="Yolcu kabin içi Acil Sağa Çekme / SOS butonuna bastı; MRM ve Çağrı Merkezi bağlantısı aktif.",
            )

        # 2. Kapı veya bagaj açıksa kalkış engellenir (Door Interlock)
        if not cabin.all_doors_closed or not cabin.trunk_closed:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=True,
                trigger_passenger_mrm=(vehicle_speed_mps > 0.5),
                intercom_call_center_active=False,
                fleet_state_recommendation="HOLD_DOOR_OR_BELT",
                max_power_derating_ratio=0.0,
                reason="Kapı veya bagaj açık (Door Interlock Aktif) — elektronik park freni kilitli.",
            )

        # 3. Yolcu oturuyor ancak emniyet kemeri takılı değilse
        if cabin.passenger_seated and not cabin.seatbelt_fastened and vehicle_speed_mps < 0.5:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=True,
                trigger_passenger_mrm=False,
                intercom_call_center_active=False,
                fleet_state_recommendation="HOLD_DOOR_OR_BELT",
                max_power_derating_ratio=0.0,
                reason="Yolcu emniyet kemeri takılı değil — kabin sesli uyarı aktif, kalkış bekliyor.",
            )

        # 4. Batarya sıcaklığı yüksekse termal güç sınırlaması (Thermal Derating)
        power_ratio = 1.0
        if bms.pack_temp_c >= self.thermal_derate_temp_c:
            power_ratio = 0.65

        # 5. Batarya şarj seviyesi (SoC) kritik eşiğin altındaysa şarj istasyonuna yönlendir
        if bms.soc_percent < self.min_dispatch_soc_percent and not cabin.passenger_seated:
            return CabinSafetyDecision(
                dispatch_allowed=False,
                motion_inhibit_brake_hold=False,
                trigger_passenger_mrm=False,
                intercom_call_center_active=False,
                fleet_state_recommendation="RETURN_TO_CHARGER",
                max_power_derating_ratio=power_ratio,
                reason=f"Batarya SoC düşük (%{bms.soc_percent:.1f} < %{self.min_dispatch_soc_percent:.1f}); araç otomatik şarj istasyonuna yönlendirildi.",
            )

        state = "IN_RIDE" if cabin.passenger_seated else "READY_FOR_PASSENGER"
        return CabinSafetyDecision(
            dispatch_allowed=True,
            motion_inhibit_brake_hold=False,
            trigger_passenger_mrm=False,
            intercom_call_center_active=False,
            fleet_state_recommendation=state,
            max_power_derating_ratio=power_ratio,
            reason=f"Kabin kapı/kemer kilitleri tam, Batarya SoC %{bms.soc_percent:.1f} ({bms.estimated_range_km:.0f} km menzil).",
        )
