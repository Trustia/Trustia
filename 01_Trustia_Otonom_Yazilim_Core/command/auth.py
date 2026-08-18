"""
TRUSTIA Komuta Merkezi (Sistem 3) — Kullanıcı rolleri ve erişim kontrolü.

Kullanıcı rolleri (PLAN 3.5): yönetici, operatör, izleyici, denetçi.
Yetkilendirme (PLAN 3.6 tabanı): rol tabanlı erişim — her işlem bir
izinle eşleşir, `require` yetkisiz çağrıda reddeder.
"""

from __future__ import annotations

from enum import IntEnum
from typing import Dict, Optional


class Role(IntEnum):
    VIEWER = 0   # izleyici: yalnızca izler
    OPERATOR = 1  # operatör: görev verir, araç komut eder
    AUDITOR = 2  # denetçi: log ve rapor okur
    ADMIN = 3    # yönetici: filo ve rol yönetimi


class Permission(IntEnum):
    VIEW = 0                # canlı görünüm, telemetri
    READ_LOG = 1            # sicil, raporlar
    COMMAND = 2             # araç komutları (başlat/durdur/acil durma)
    ASSIGN_MISSION = 3      # görev atama
    MANAGE_FLEET = 4        # araç kaydı
    MANAGE_ROLES = 5        # rol yönetimi


ROLE_PERMISSIONS: Dict[Role, set] = {
    Role.VIEWER: {Permission.VIEW},
    Role.OPERATOR: {
        Permission.VIEW,
        Permission.COMMAND,
        Permission.ASSIGN_MISSION,
    },
    Role.AUDITOR: {Permission.VIEW, Permission.READ_LOG},
    Role.ADMIN: set(Permission),
}


class AccessDenied(PermissionError):
    """Yetkisiz işlem denemesi — denetim kaydına düşer."""


class AccessControl:
    """Kullanıcı → rol → izin eşlemesi."""

    def __init__(self) -> None:
        self._roles: Dict[str, Role] = {}

    def set_role(self, user: str, role: Role) -> None:
        self._roles[user] = role

    def role_of(self, user: str) -> Role:
        return self._roles.get(user, Role.VIEWER)

    def unregister(self, user: str) -> None:
        self._roles.pop(user, None)

    def can(self, user: str, permission: Permission) -> bool:
        return permission in ROLE_PERMISSIONS[self.role_of(user)]

    def require(self, user: str, permission: Permission) -> None:
        """Yetki yoksa AccessDenied yükseltir — komut engelleme noktası."""
        if not self.can(user, permission):
            raise AccessDenied(
                f"{user} ({self.role_of(user).name}) "
                f"'{permission.name}' iznine sahip değil"
            )

    def list_users(self) -> Dict[str, str]:
        return {u: r.name for u, r in sorted(self._roles.items())}

    def role_permissions(self, role: Role) -> list:
        return sorted(p.name for p in ROLE_PERMISSIONS[role])


class Session:
    """Tek oturum: kullanıcı kimliği + erişim kontrolü bağlantısı."""

    def __init__(self, user: str, access: AccessControl) -> None:
        self.user = user
        self.access = access

    def require(self, permission: Permission) -> None:
        self.access.require(self.user, permission)

    def can(self, permission: Permission) -> bool:
        return self.access.can(self.user, permission)
