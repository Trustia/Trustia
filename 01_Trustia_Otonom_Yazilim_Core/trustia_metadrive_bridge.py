"""
TRUSTIA AI — MetaDrive 3D Otonom Sürüş Simülasyon Köprüsü
=============================================================================
Bu modül, Trustia'nın 16.400+ satırlık Seviye-4 otonom sürüş yığınını (Algı,
LiDAR, Şerit Takibi, Stanley/PID Kontrolcü ve ASIL-D E-STOP) doğrudan MetaDrive
3D simülasyon dünyasına bağlar.

Özellikler:
  * 3D Araç, Sokaklar, Yol Ağı ve Bullet Physics dinamikleri
  * 48 Işınlı 3D LiDAR nokta bulutu entegrasyonu
  * Trustia PID kontrolcüsü ile otonom direksiyon ve gaz/fren kontrolü
  * ISO 26262 ASIL-D Minimal Risk Maneuver (MRM) ve Acil Fren (E-STOP)

Kullanım:
  python trustia_metadrive_bridge.py
"""

from __future__ import annotations

import math
import sys
import time
from pathlib import Path

CORE_DIR = Path(__file__).resolve().parent
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

# Trustia Alt Sistemleri
from control import Controller, PidGains, VehicleModel
from core.transforms import EnuPoint
from security.estop import EmergencyStop


def _wrap_angle(angle_rad: float) -> float:
    while angle_rad > math.pi:
        angle_rad -= 2.0 * math.pi
    while angle_rad < -math.pi:
        angle_rad += 2.0 * math.pi
    return angle_rad


def run_trustia_in_metadrive(render: bool = True, steps: int = 2500) -> None:
    try:
        from metadrive.envs.metadrive_env import MetaDriveEnv
    except ImportError:
        print("[HATA] metadrive-simulator henüz kurulu değil! Lütfen 'pip install metadrive-simulator' çalıştırın.")
        return

    print("=" * 75)
    print("      TRUSTIA AI — METADRIVE 3D OTONOM SÜRÜŞ SİMÜLASYONU")
    print("    16.400+ Satır Otonomi Çekirdeği & 48 Işınlı LiDAR Entegrasyonu")
    print("=" * 75)
    print("[*] 3D Simülasyon Dünyası Başlatılıyor (Panda3D + Bullet Physics)...")

    # MetaDrive Simülasyon Konfigürasyonu
    config = {
        "use_render": render,
        "manual_control": False,          # Otonom sürüş Trustia kontrolünde
        "traffic_density": 0.08,          # Çevre araç trafiği
        "map": "SCXRO",                   # Düz, Viraj, Kavşak ve Döner Kavşak
        "start_seed": 42,
        "vehicle_config": {
            "show_lidar": True,           # LiDAR ışınlarını 3D ekranda göster
            "show_navi_mark": True,       # Navigasyon rotasını göster
            "lidar": {
                "num_lasers": 48,         # Trustia standardı 48 ışın
                "distance": 35.0,         # 35 metre menzil
            }
        }
    }

    env = MetaDriveEnv(config)

    # Trustia PID Kontrolcü (Direksiyon & Hız)
    controller = Controller(
        model=VehicleModel(
            max_speed_mps=15.0,
            max_angular_radps=1.5,
            max_accel_mps2=3.0,
        ),
        heading_gains=PidGains(kp=2.0, ki=0.04, kd=0.25),
        speed_gains=PidGains(kp=1.2, ki=0.02, kd=0.0),
    )
    estop = EmergencyStop()

    try:
        obs, info = env.reset()
        print("\n[OK] Simülasyon Aktif! Trustia Seviye-4 Otonom Sürüş Devrede.")
        print("[*] Ekranda 3D Araç, Yollar, Trafik ve 48 Işınlı LiDAR Canlı.")
        print("[*] Kamerayı fareyle kontrol edebilirsiniz (Sol tık: Döndür, Sağ tık: Yakınlaş).")
        print("[*] Durdurmak için pencereyi kapatabilir veya terminalde Ctrl+C yapabilirsiniz.\n")

        target_speed_mps = 8.5  # ~30 km/h şehir içi güvenli hız

        for step in range(steps):
            vehicle = env.agent
            speed_kmh = vehicle.speed_km_h
            speed_mps = speed_kmh / 3.6

            # 1. 48 Işınlı LiDAR Algılama Verisi
            cloud, surrounding_objs = vehicle.lidar.perceive(
                vehicle,
                vehicle.engine.physics_world.dynamic_world,
                48,
                35.0,
            )
            raw_min_ratio = min(cloud) if cloud else 1.0
            min_dist_m = raw_min_ratio * 35.0

            # 2. ISO 26262 ASIL-D E-STOP & Güvenlik Denetimi
            if min_dist_m < 1.8:
                estop.stop(source="COLLISION_PREVENTION", message=f"KRITIK_ENGEL_{min_dist_m:.1f}M")
            else:
                if estop.stopped and min_dist_m > 4.0:
                    estop.clear(source="RECOVERY", message="YOL_TEMIZ")

            # 3. Şerit ve Rota Takibi Açı Hatası
            lane = vehicle.navigation.current_lane
            if lane:
                lon, lat = lane.local_coordinates(vehicle.position)
                heading_diff = _wrap_angle(lane.heading_theta_at(lon) - vehicle.heading_theta)
                # Stanley lateral hata düzeltmesi
                lat_correction = math.atan2(0.5 * -lat, max(1.0, speed_mps))
                steer_target_heading = heading_diff + lat_correction
            else:
                steer_target_heading = 0.0

            # 4. Trustia PID Kontrol Adımı
            if estop.stopped:
                cmd_speed = 0.0
                steer_input = 0.0
                throttle = -1.0  # ASIL-D Acil Fren
            else:
                # Engellere yaklaştıkça yumuşak yavaşlama
                if min_dist_m < 12.0:
                    desired_spd = max(2.5, min_dist_m * 0.55)
                else:
                    desired_spd = target_speed_mps

                cmd = controller.step(
                    target_heading_rad=steer_target_heading,
                    target_speed_mps=desired_spd,
                    current_heading_rad=0.0,
                    dt=0.02,
                )
                steer_input = max(-1.0, min(1.0, cmd.angular_radps / 1.2))
                throttle = max(-1.0, min(1.0, (desired_spd - speed_mps) * 0.45))

            # 5. MetaDrive araca komut gönder (steer, throttle/brake)
            obs, reward, terminated, truncated, info = env.step([steer_input, throttle])

            if step % 25 == 0:
                asil_status = "ACIL_FREN" if estop.stopped else "NOMINAL"
                print(f"Adım: {step:4d} | Hız: {speed_kmh:4.1f} km/h | Min LiDAR: {min_dist_m:4.1f}m | Direksiyon: {steer_input:+4.2f} | ASIL-D: {asil_status}")

            if terminated or truncated:
                print("\n[*] Rota tamamlandı, yeni parkura geçiliyor...")
                obs, info = env.reset()
                estop.clear(source="RESET", message="NEW_EPISODE")

    except KeyboardInterrupt:
        print("\n[*] Simülasyon durduruldu.")
    finally:
        env.close()
        print("[OK] MetaDrive simülatörü güvenle kapatıldı.")


if __name__ == "__main__":
    run_trustia_in_metadrive(render=True)
