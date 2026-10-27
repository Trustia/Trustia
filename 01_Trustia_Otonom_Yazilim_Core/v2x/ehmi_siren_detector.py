"""
TRUSTIA ISO/TR 23049 Dış İnsan-Makine Arayüzü (eHMI) ve Akustik Ambulans/İtfaiye Siren Algılayıcısı
===================================================================================================
AB 2022/1426 (1 Aralık 2024 Resmî Gazete) Ek-II İnsan Faktörleri ve Acil Araç Önceliği gereksinimleri:
  1. Dış İnsan-Makine Arayüzü (eHMI - External Human-Machine Interface):
     Sürücüsüz robotakside direksiyon başında göz teması kuracak bir insan sürücü bulunmadığından,
     yaya geçidindeki yayalara ve dış trafiğe aracın niyetini (Yol Veriliyor / Otonom Sürüş Aktif /
     Kalkışa Hazırlanıyor / Acil Sağa Çekme) dış LED panel ve akustik uyarı ile bildirir.
  2. Akustik Acil Durum Siren Algılayıcısı (600 Hz - 1500 Hz Wail/Yelp Bandı):
     V2X vericisi olmayan ambulans, itfaiye veya polis araçlarının siren sesini dış mikrofon
     frekans spektrumundan ve ses şiddetinden (dB) algılayarak otomatik sağa çekme (Corridor Yield)
     manevrası başlatır.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EhmiAndSirenDecision:
    """Dış yaya iletişim paneli (eHMI) ve akustik siren denetimi çıktısı."""

    ehmi_display_state: str     # "YIELDING_PEDESTRIAN_CROSS", "EMERGENCY_CORRIDOR_YIELD", "MRM_HAZARD_STOP", "AUTONOMOUS_CRUISE"
    ehmi_led_color_rgb: str     # "#00E5FF" (Turkuaz/Otonom), "#10B981" (Yeşil/Yaya Geçişi), "#F59E0B" (Kehribar/Uyarı)
    external_chime_active: bool
    emergency_siren_detected: bool
    recommended_vehicle_action: str  # "MAINTAIN_COURSE", "STOP_AND_SIGNAL_PEDESTRIAN", "PULL_OVER_RIGHT_EMERGENCY"
    detail: str


class ExternalHmiAndSirenSupervisor:
    """
    ISO/TR 23049 uyumlu dış yaya iletişim (eHMI) ve akustik acil durum aracı (ambulans/itfaiye)
    siren algılama denetleyicisi.
    """

    def __init__(
        self,
        siren_min_freq_hz: float = 600.0,
        siren_max_freq_hz: float = 1550.0,
        siren_min_spl_db: float = 78.0,
    ) -> None:
        self.siren_min_freq_hz = siren_min_freq_hz
        self.siren_max_freq_hz = siren_max_freq_hz
        self.siren_min_spl_db = siren_min_spl_db

    def evaluate(
        self,
        yielding_to_pedestrian: bool,
        mrm_active: bool,
        dominant_audio_freq_hz: float = 120.0,
        audio_spl_db: float = 55.0,
        freq_modulation_detected: bool = False,
    ) -> EhmiAndSirenDecision:
        """Akustik spektrumu ve araç davranış durumunu değerlendirerek eHMI ve manevra kararı üretir."""
        siren_in_band = self.siren_min_freq_hz <= dominant_audio_freq_hz <= self.siren_max_freq_hz
        siren_detected = siren_in_band and (audio_spl_db >= self.siren_min_spl_db) and freq_modulation_detected

        # 1. Ambulans / İtfaiye / Polis sireni algılandıysa mutlak öncelik
        if siren_detected:
            return EhmiAndSirenDecision(
                ehmi_display_state="EMERGENCY_CORRIDOR_YIELD",
                ehmi_led_color_rgb="#F59E0B",
                external_chime_active=True,
                emergency_siren_detected=True,
                recommended_vehicle_action="PULL_OVER_RIGHT_EMERGENCY",
                detail=f"Akustik acil durum sireni algılandı ({dominant_audio_freq_hz:.0f} Hz, {audio_spl_db:.1f} dB) — sağa fermuar koridoru açılıyor.",
            )

        # 2. Arıza veya MRM durumu
        if mrm_active:
            return EhmiAndSirenDecision(
                ehmi_display_state="MRM_HAZARD_STOP",
                ehmi_led_color_rgb="#EF4444",
                external_chime_active=True,
                emergency_siren_detected=False,
                recommended_vehicle_action="PULL_OVER_RIGHT_EMERGENCY",
                detail="MRM güvenli duruş aktif — dış uyarı flaşörleri ve eHMI tehlike modu açık.",
            )

        # 3. Yaya geçidinde yayaya yol verme durumu
        if yielding_to_pedestrian:
            return EhmiAndSirenDecision(
                ehmi_display_state="YIELDING_PEDESTRIAN_CROSS",
                ehmi_led_color_rgb="#10B981",
                external_chime_active=True,
                emergency_siren_detected=False,
                recommended_vehicle_action="STOP_AND_SIGNAL_PEDESTRIAN",
                detail="ISO/TR 23049 eHMI: Yayaya güvenli geçiş işareti gösteriliyor.",
            )

        return EhmiAndSirenDecision(
            ehmi_display_state="AUTONOMOUS_CRUISE",
            ehmi_led_color_rgb="#00E5FF",
            external_chime_active=False,
            emergency_siren_detected=False,
            recommended_vehicle_action="MAINTAIN_COURSE",
            detail="Standart Seviye-4 otonom sürüş eHMI aydınlatması aktif.",
        )
