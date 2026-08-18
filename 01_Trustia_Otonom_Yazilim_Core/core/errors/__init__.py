"""
TRUSTIA Hata Yönetimi — Seviyeli hata sınıfı hiyerarşisi.

Hata seviyeleri:
  * TrustiaError      : Tüm TRUSTIA hatalarının kökü
  * RecoverableError  : Kurtarılabilir (yeniden deneme mantığı başlat)
  * ConfigurationError: Ayar/yapılandırma hataları
  * SensorError       : Sensör okuma/bağlantı hataları
  * CommunicationError: Haberleşme kesintileri
  * NavigationError   : Konum/rota hesaplama hataları
  * ControlError      : Denetleyici/aktüatör hataları
  * SafetyError       : Güvenlik ihlalleri (en kritik seviye)

Kurtarma politikası, hata sınıfının 'recoverable' niteliği ile
yönlendirilir; güvenlik hataları her zaman acil durma tetikler.
"""

from __future__ import annotations

from enum import IntEnum


class ErrorSeverity(IntEnum):
    INFO = 10
    WARNING = 20
    RECOVERABLE = 30
    FATAL = 40
    SAFETY = 50


class TrustiaError(Exception):
    """Tüm TRUSTIA hatalarının kök sınıfı."""

    severity = ErrorSeverity.FATAL
    recoverable = False
    safety_critical = False

    def __init__(self, message: str, *, details: object = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details

    def describe(self) -> str:
        base = f"{type(self).__name__}: {self.message}"
        if self.details is not None:
            base += f" | detay: {self.details}"
        return base


class RecoverableError(TrustiaError):
    """Yeniden deneme veya alternatif yolla kurtarılabilecek hatalar."""

    severity = ErrorSeverity.RECOVERABLE
    recoverable = True


class ConfigurationError(TrustiaError):
    """Eksik/geçersiz yapılandırma."""

    severity = ErrorSeverity.FATAL


class SensorError(RecoverableError):
    """Sensör okuma, kalibrasyon veya bağlantı hataları."""

    severity = ErrorSeverity.RECOVERABLE


class CommunicationError(RecoverableError):
    """Araç içi/dışı haberleşme kesintileri."""

    severity = ErrorSeverity.RECOVERABLE


class NavigationError(RecoverableError):
    """Konum, harita veya rota hesaplama hataları."""

    severity = ErrorSeverity.RECOVERABLE


class ControlError(RecoverableError):
    """Denetleyici hesaplama veya aktüatör komut hataları."""

    severity = ErrorSeverity.RECOVERABLE


class PlanningError(RecoverableError):
    """Rota bulma başarısızlıkları (geçit bulunamadı vb.)."""

    severity = ErrorSeverity.RECOVERABLE


class SafetyError(TrustiaError):
    """Güvenlik ihlalleri — acil durma gerektirir."""

    severity = ErrorSeverity.SAFETY
    safety_critical = True
