"""
TRUSTIA AŞAMA 4 — Güvenlik (Sistem 5) + JAUS/Entegrasyon (Sistem 8) gösterisi.

Akış: GCS'ten JAUS komutu (AS6009/AS6091 Mobility) -> araçta güvenlik
süzgeci (komut doğrulama + acil durma + bağlantı kaybı) -> CAN bus'a
motor/direksiyon komutu -> tüm olaylar denetim kaydında.

Çalıştırma:  python demos/asama4_guvenlik_demo.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command import CommandCenter, MissionOrder
from command.auth import Role
from core.api import Command, CommandType
from core.transforms import EnuPoint
from integration import (
    CanBus,
    JausEndpoint,
    MobilityService,
    VehicleHardware,
    command_to_message,
    message_to_command,
)
from integration.can import ID_MOTOR_SPEED, MotorController
from record import MissionRecorder, MissionReport, Replay
from security import Shield
from simulation.runner import MissionRunner
from simulation.terrain import Terrain, Weather

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "reports", "asama4",
)


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shield = Shield(OUT_DIR, link_key=b"TRUSTIA-ASAMA4-ortak-sir-32-bayt")

    gcs = JausEndpoint(0x1001, "GCS")
    araç = JausEndpoint(0x2001, "ARAÇ-01")
    mobility = MobilityService(gcs)
    hardware = VehicleHardware()

    print("== AŞAMA 4 — GÜVENLİK + JAUS/ENTEGRASYON GÖSTERİSİ ==")

    def run_command(command: Command, who: str) -> bool:
        jaus_message = command_to_message(command, gcs.uid, araç.uid)
        raw = gcs.send(jaus_message)
        received = araç.receive(raw)
        back = message_to_command(received)
        print(
            f"  [{who}] {back.command_type.name} "
            f"-> JAUS {received.message_code:#06x} "
            f"-> {len(raw)} bayt"
        )
        speed = back.params.get("speed_mps")
        result = shield.validate_command(
            who, back.command_type.name,
            speed_mps=speed if speed is not None else 1.0,
            target_m=(30.0, 30.0),
        )
        if not result.valid:
            print(f"    REDDEDİLDİ: {result.reason}")
            return False
        frames = hardware.drive(speed or 0.0, 0.0)
        speed_out = MotorController.decode_speed(frames[0])
        print(f"    CAN: motor {speed_out} m/s, direksiyon 0.0 rad "
              f"({hardware.tx_count()} çerçeve toplam)")
        return True

    print("\n1) JAUS KOMUT KANALI (GCS -> araç)")
    run_command(Command(command_id=1, command_type=CommandType.SET_SPEED,
                        params={"speed_mps": 1.5}), "op")
    print("   operatör acil durma gönderiyor:")
    stop_result = run_command(
        Command(command_id=2, command_type=CommandType.EMERGENCY_STOP), "op"
    )
    shield.emergency_stop("yazılımsal", "JAUS EMERGENCY_STOP alındı")
    print("   (acil durumda sürüş komutu engelleniyor)")
    run_command(Command(command_id=3, command_type=CommandType.SET_SPEED,
                        params={"speed_mps": 1.0}), "op")
    shield.emergency_clear("operatör", "kontrol tamam")
    print("   (acil durum açıldı — sürüş yeniden serbest)")
    run_command(Command(command_id=4, command_type=CommandType.SET_SPEED,
                        params={"speed_mps": 0.8}), "op")

    print("\n2) BAĞLANTI KAYBI (link loss -> dur -> bekle -> geri dön)")
    shield.linkloss._lost_after_s = 2.5
    shield.linkloss._safe_stop_s = 1.0
    shield.linkloss._wait_before_return_s = 3.0
    print("   t=24 sn itibariyle telemetri kesiliyor ...")
    for t in range(0, 60):
        if t < 24 and t % 4 == 0:
            shield.link_frame(t)
        decision = shield.evaluate_link(t)
        if decision.is_safe_stop or decision.is_return_home:
            print(f"   t={t:>3d} sn: {decision.detail}")
        if shield.linkloss.return_requested():
            print("   -> RETURN_HOME komutu araca gönderildi (denetimde)")
    print(f"   son durum: {shield.linkloss.state.name}")

    print("\n3) GÖREV KOŞUSU (güvenlik zırhı üzerinde) + KAYIT")
    center = CommandCenter()
    center.access.set_role("admin", Role.ADMIN)
    center.access.set_role("op", Role.OPERATOR)
    center.register_vehicle("admin", "A-01", "Keşif Aracı 1")
    order = MissionOrder(
        order_id="G-A01", vehicle_id="A-01", mission_type="kesif",
        waypoints=[EnuPoint(east_m=30, north_m=30)], time_limit_s=120.0,
    )
    order_id = center.submit_mission("op", order)
    terrain = Terrain(width_m=40, height_m=40, seed=1)
    terrain.add_obstacle(15, 15, 1.5)
    terrain.add_forbidden(25, 10, 2.0)
    recorder = MissionRecorder(OUT_DIR, record_id=order_id).start()
    recorder.set_metadata(mission_id=order_id, vehicle_id="A-01",
                          mission_type="kesif", world_size_m=40.0)
    metrics = center.dispatch(
        _session(center), order_id, terrain, Weather(),
        MissionRunner(seed=3), start=(2, 2),
        telemetry_callback=recorder.record_frame,
    )
    recorder.record_result(metrics)
    recorder.close()
    print(f"   sonuç: {'BAŞARILI' if metrics.success else 'BAŞARISIZ'} "
          f"| {metrics.steps} adım | kayıt {recorder.frame_count()} çerçeve")

    replay = Replay.load(recorder.path)
    MissionReport(replay, world_size_m=40.0,
                  record_path=recorder.path).write(OUT_DIR)

    print("\n4) DENETİM KAYDI")
    rows = shield.audit_query(limit=10)
    for row in rows:
        print(f"   {row['user']:12s} {row['action']:16s} "
              f"{row['target']:8s} {row['detail'][:40]}")
    shield.close()
    _write_report()
    print("\nGUVENLIK_RAPORU_ASAMA4.md yazıldı.")


def _session(center: CommandCenter):
    from command.auth import Session
    return Session("op", center.access)


def _write_report() -> None:
    lines = [
        "# TRUSTIA GÜVENLİK VE ENTEGRASYON RAPORU (AŞAMA 4)",
        "",
        "- **Proje sürümü:** 0.4.0",
        "- **Tarih:** 2026-08-03",
        "- **Ortam:** win32, Python 3.12.10",
        "",
        "## 1. KAPSAM",
        "",
        "- **Sistem 5 — Güvenlik (Shield):** acil durma anahtarı "
        "(fiziksel + yazılımsal), bağlantı kaybı yönetimi "
        "(dur -> bekle -> geri dön), komut doğrulama (tehlikeli/geçersiz "
        "komut engelleme), HMAC-SHA256 mesaj imzalama + zaman penceresi "
        "(yeniden oynatma koruması), denetim kaydı (kim-ne-zaman-ne yaptı).",
        "- **Sistem 8 — Araç/Sensör Entegrasyonu:** CAN/CAN FD katmanı "
        "(motor/direksiyon komutları), çok marka LiDAR ve kamera sürücü "
        "soyutlaması, donanım soyutlama katmanı, JAUS mesaj katmanı "
        "(AS6009/AS6091 temelli — Mobility, Positioning, Payload servisleri) "
        "ve core.api komut eşlemesi.",
        "",
        "## 2. GÖSTERİ",
        "",
        "1. **JAUS komut kanalı:** GCS -> MobilityService (SetSpeed) -> "
        "araç uç noktası -> core.api komutuna eşleme -> güvenlik süzgeci -> "
        "CAN motor/direksiyon çerçeveleri.",
        "2. **Acil durum:** operatör EMERGENCY_STOP gönderir; aynı döngüdeki "
        "sürüş komutu güvenlik süzgeci tarafından reddedilir "
        "('acil durumda sürüş komutu engellendi').",
        "3. **Bağlantı kaybı:** telemetri kesilir; araç güvenli durma, "
        "bekleme ve ardından ana üsse dönme (RETURN_HOME) davranışını "
        "uygular; dönüş komutu bir kez üretilir ve denetime düşer.",
        "4. **Görev koşusu:** komuta merkezi görevi simülasyonda koşturur; "
        "kayıt ve rapor üretilir (asama4/G-A01.*).",
        "",
        "## 3. KANIT DOSYALARI",
        "",
        "- `asama4/denetim.jsonl` — tüm güvenlik olayları.",
        "- `asama4/G-A01.jsonl` — görev kaydı (telemetri + sonuç).",
        "- `asama4/G-A01.md` + SVG grafikler — görev raporu.",
        "",
        "## 4. GÜVENLİK KONTROL LİSTESİ",
        "",
        "| PLAN 3.6 maddesi | Durum |",
        "|---|---|",
        "| Bağlantı kaybında güvenli durma | uygulandı (LinkLossManager) |",
        "| Komut doğrulama: geçersiz/tehlikeli komut engelleme | uygulandı (CommandGuard) |",
        "| Yetkilendirme: rol tabanlı erişim | uygulandı (Sistem 3 auth) |",
        "| Mesaj bütünlüğü + yeniden oynatma koruması | uygulandı (HMAC-SHA256) |",
        "| Denetim kaydı | uygulandı (AuditLog) |",
        "| Acil durma anahtarı protokolü | uygulandı (EmergencyStop, fiziksel+yazılımsal) |",
        "",
        "## 5. YORUM",
        "",
        "- JAUS uç noktaları arasındaki mesajlaşma 32 baytlık sabit başlık + "
        "JSON gövdeyle birebir kodlanıp çözülür; servis ayrımı "
        "(Mobility/Positioning/Payload) başlıkta taşınır.",
        "- Güvenlik zinciri fail-safe'dir: acil durum veya bağlantı kaybında "
        "sürüş komutları zincir tarafından engellenir; açık kurtarma "
        "olmadan araç hareket edemez.",
        "",
    ]
    path = os.path.join(os.path.dirname(OUT_DIR), "GUVENLIK_RAPORU_ASAMA4.md")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


if __name__ == "__main__":
    main()
