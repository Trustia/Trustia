"""
TRUSTIA ISO/TR 23049 Dış İnsan-Makine Arayüzü (eHMI) ve Akustik Ambulans/İtfaiye Siren Algılayıcısı
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EhmiAndSirenDecision:
    ehmi_display_state: str
    ehmi_led_color_rgb: str
    external_chime_active: bool
    emergency_siren_detected: bool
    recommended_vehicle_action: str
    detail: str


class ExternalHmiAndSirenSupervisor:
    """ISO/TR 23049 dış yaya iletişim (eHMI) ve akustik siren algılama denetleyicisi."""

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
        siren_detected = (
            self.siren_min_freq_hz <= dominant_audio_freq_hz <= self.siren_max_freq_hz
            and audio_spl_db >= self.siren_min_spl_db
            and freq_modulation_detected
        )
        if siren_detected:
            return EhmiAndSirenDecision(
                "EMERGENCY_CORRIDOR_YIELD",
                "#F59E0B",
                True,
                True,
                "PULL_OVER_RIGHT_EMERGENCY",
                "Akustik ambulans/itfaiye sireni algılandı.",
            )
        if mrm_active:
            return EhmiAndSirenDecision(
                "MRM_HAZARD_STOP",
                "#EF4444",
                True,
                False,
                "PULL_OVER_RIGHT_EMERGENCY",
                "MRM tehlike modu aktif.",
            )
        if yielding_to_pedestrian:
            return EhmiAndSirenDecision(
                "YIELDING_PEDESTRIAN_CROSS",
                "#10B981",
                True,
                False,
                "STOP_AND_SIGNAL_PEDESTRIAN",
                "Yayaya güvenli geçiş işareti gösteriliyor.",
            )
        return EhmiAndSirenDecision(
            "AUTONOMOUS_CRUISE",
            "#00E5FF",
            False,
            False,
            "MAINTAIN_COURSE",
            "Otonom sürüş eHMI aktif.",
        )
