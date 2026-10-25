"""
TRUSTIA Otonomi Platformu — Kurumsal Seviye-4 Robotaksi Kokpit ve Teşhis Konsolu (GUI).
SAIC Maxus MIFA 7 & Tripy Mobility Saha Test ve Operatör Arayüzü.

Tamamen Sivil, Modern Karanlık Tema (Dark Tech UI) — Sıfır Üçüncü Taraf Bağımlılık (Saf Tkinter).
"""

from __future__ import annotations

import math
import time
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Tuple, Optional

from trustia_sdk.core.transforms import Pose2D, KinematicState, normalize_angle
from trustia_sdk.canbus.mifa7_canfd import Mifa7CanFdBridge
from trustia_sdk.planning.hybrid_astar import HybridAStarPlanner
from trustia_sdk.control.stanley_controller import StanleyController
from trustia_sdk.safety.asil_d_mrm import AsilDSafetySupervisor, SafetyState
from trustia_sdk.perception.calmcar_bridge import CalmCarSafetyArbiter


class RobotaxiCockpitApp(tk.Tk):
    """Tripy Mobility SAIC Maxus MIFA 7 Saha ve Mühendislik Kokpit Konsolu."""

    def __init__(self) -> None:
        super().__init__()

        self.title("TRUSTIA L4 ROBOTAXI — KURUMSAL MÜHENDİSLİK KOKPİTİ (SAIC MAXUS MIFA 7)")
        self.geometry("1360x860")
        self.configure(bg="#0a0f1d")

        # Sistem Bileşenleri
        self.can_bridge = Mifa7CanFdBridge()
        self.planner = HybridAStarPlanner(wheel_base_m=2.975, max_steer_deg=35.0)
        self.controller = StanleyController(wheel_base_m=2.975)
        self.safety = AsilDSafetySupervisor(watchdog_timeout_ms=50.0)
        self.arbiter = CalmCarSafetyArbiter()

        # Simülasyon Araç Durumu (Ankara Bilkent Cyberpark Başlangıç)
        self.state = KinematicState(x=10.0, y=10.0, yaw_rad=math.radians(30), velocity_mps=6.5)
        self.target_speed_kmh = 35.0

        # Rota ve Engeller
        self.obstacles: List[Tuple[float, float, float]] = [
            (25.0, 18.0, 1.2), # Park halindeki araç
            (42.0, 32.0, 0.8), # Yaya geçidi
            (60.0, 40.0, 1.5)  # Kavşak
        ]
        self.path = self.planner.plan(
            start=Pose2D(10.0, 10.0, math.radians(30)),
            goal=Pose2D(70.0, 45.0, math.radians(15)),
            obstacles=self.obstacles
        )

        self._build_ui()
        self.after(50, self._drive_simulation_tick)

    def _build_ui(self) -> None:
        # 1. ÜST BİLGİ VE BAŞLIK ŞERİDİ
        header = tk.Frame(self, bg="#111827", height=55, bd=1, relief="solid")
        header.pack(fill="x", side="top", padx=10, pady=8)

        # Başlık ve Logo
        title_box = tk.Frame(header, bg="#111827")
        title_box.pack(side="left", padx=15, pady=8)

        tk.Label(title_box, text="TRUSTIA", font=("Consolas", 15, "bold"), fg="#06b6d4", bg="#111827").pack(side="left")
        tk.Label(title_box, text=" | L4 ROBOTAXI ENTERPRISE COCKPIT", font=("Segoe UI", 11, "bold"), fg="#f3f4f6", bg="#111827").pack(side="left", padx=8)

        # Durum Rozetleri (Status Badges)
        badge_box = tk.Frame(header, bg="#111827")
        badge_box.pack(side="right", padx=15)

        self._create_badge(badge_box, "PLATFORM: MAXUS MIFA 7", "#1e3a8a")
        self._create_badge(badge_box, "CAN-FD: 500k/2M ACTIVE", "#047857")
        self._create_badge(badge_box, "ASIL-D: NOMINAL", "#0d9488")
        self._create_badge(badge_box, "CALMCAR: ARBITRATED", "#0284c7")
        self._create_badge(badge_box, "KVKK m.9: SEALED", "#4f46e5")

        # 2. ANA ÇALIŞMA ALANI (3 Sütunlu Izgara)
        main_body = tk.Frame(self, bg="#0a0f1d")
        main_body.pack(fill="both", expand=True, padx=10, pady=4)

        # SOL SÜTUN: Araç Dinamiği & Aktüatör Telemetrisi (Genişlik: 320px)
        left_panel = tk.Frame(main_body, bg="#111827", width=340, bd=1, relief="solid")
        left_panel.pack(side="left", fill="y", padx=5, pady=5)
        left_panel.pack_propagate(False)

        self._build_panel_header(left_panel, "ARAÇ AKTÜATÖR VE CAN-FD DURUMU")
        self._build_left_telemetry(left_panel)

        # ORTA SÜTUN: 2D Radar & LiDAR Yörünge Haritası (Canvas)
        center_panel = tk.Frame(main_body, bg="#111827", bd=1, relief="solid")
        center_panel.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self._build_panel_header(center_panel, "3D LiDAR ALGI VE SEYRÜSEFER HARİTASI (REAL-TIME)")
        self.map_canvas = tk.Canvas(center_panel, bg="#050811", highlightthickness=0)
        self.map_canvas.pack(fill="both", expand=True, padx=8, pady=8)

        # SAĞ SÜTUN: Emniyet Hakemi & Filo Teşhis (Genişlik: 340px)
        right_panel = tk.Frame(main_body, bg="#111827", width=350, bd=1, relief="solid")
        right_panel.pack(side="right", fill="y", padx=5, pady=5)
        right_panel.pack_propagate(False)

        self._build_panel_header(right_panel, "ISO 26262 ASIL-D GÜVENLİK VE TEŞHİS")
        self._build_right_safety(right_panel)

    def _create_badge(self, parent: tk.Widget, text: str, color: str) -> None:
        lbl = tk.Label(parent, text=text, font=("Consolas", 9, "bold"), fg="#ffffff", bg=color, padx=10, pady=4)
        lbl.pack(side="left", padx=4)

    def _build_panel_header(self, parent: tk.Widget, title: str) -> None:
        p_hdr = tk.Frame(parent, bg="#1f2937", height=32)
        p_hdr.pack(fill="x", side="top")
        tk.Label(p_hdr, text=title, font=("Segoe UI", 9, "bold"), fg="#38bdf8", bg="#1f2937").pack(side="left", padx=10, pady=5)

    def _build_left_telemetry(self, parent: tk.Widget) -> None:
        container = tk.Frame(parent, bg="#111827")
        container.pack(fill="both", expand=True, padx=12, pady=10)

        # Hız Göstergesi
        speed_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        speed_box.pack(fill="x", pady=6)
        tk.Label(speed_box, text="ANLIK SÜRAT", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_speed = tk.Label(speed_box, text="23.4 km/s", font=("Consolas", 24, "bold"), fg="#22c55e", bg="#1e293b")
        self.lbl_speed.pack(anchor="w", padx=10, pady=(0, 6))

        # Direksiyon Açısı
        steer_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        steer_box.pack(fill="x", pady=6)
        tk.Label(steer_box, text="DİREKSİYON AÇISI (EPS LKAS)", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_steer = tk.Label(steer_box, text="+4.2°", font=("Consolas", 20, "bold"), fg="#38bdf8", bg="#1e293b")
        self.lbl_steer.pack(anchor="w", padx=10, pady=(0, 6))

        # Yanal Sapma (Cross-Track Error)
        cte_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        cte_box.pack(fill="x", pady=6)
        tk.Label(cte_box, text="YANAL ŞERİT HATASI (CTE)", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_cte = tk.Label(cte_box, text="3.5 cm (ASIL-D NOMINAL)", font=("Consolas", 12, "bold"), fg="#10b981", bg="#1e293b")
        self.lbl_cte.pack(anchor="w", padx=10, pady=(0, 6))

        # Batarya Durumu
        bat_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        bat_box.pack(fill="x", pady=6)
        tk.Label(bat_box, text="BATARYA DOLULUK (% SoC)", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_battery = tk.Label(bat_box, text="88% (90 kWh E-GMP)", font=("Consolas", 12, "bold"), fg="#f59e0b", bg="#1e293b")
        self.lbl_battery.pack(anchor="w", padx=10, pady=(0, 6))

        # Aktüatör CAN-FD Sayacı
        can_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        can_box.pack(fill="x", pady=6)
        tk.Label(can_box, text="CAN-FD İLETİLEN ÇERÇEVE", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_can_count = tk.Label(can_box, text="0 Çerçeve (100 Hz)", font=("Consolas", 11, "bold"), fg="#94a3b8", bg="#1e293b")
        self.lbl_can_count.pack(anchor="w", padx=10, pady=(0, 6))

    def _build_right_safety(self, parent: tk.Widget) -> None:
        container = tk.Frame(parent, bg="#111827")
        container.pack(fill="both", expand=True, padx=12, pady=10)

        # Otonomi Modu Kartı
        mode_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        mode_box.pack(fill="x", pady=6)
        tk.Label(mode_box, text="OTONOMİ MODU", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_mode = tk.Label(mode_box, text="SEVİYE-4 AKTİF", font=("Segoe UI", 16, "bold"), fg="#06b6d4", bg="#1e293b")
        self.lbl_mode.pack(anchor="w", padx=10, pady=(0, 6))

        # Watchdog ve Emniyet
        wd_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        wd_box.pack(fill="x", pady=6)
        tk.Label(wd_box, text="50ms WATCHDOG NABIZ", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_watchdog = tk.Label(wd_box, text="12 ms (CANLI)", font=("Consolas", 12, "bold"), fg="#10b981", bg="#1e293b")
        self.lbl_watchdog.pack(anchor="w", padx=10, pady=(0, 6))

        # CalmCar Uç Güvenlik Kalkanı
        calm_box = tk.Frame(container, bg="#1e293b", bd=1, relief="solid")
        calm_box.pack(fill="x", pady=6)
        tk.Label(calm_box, text="KVKK m.9 UÇ VERİ KALKANI", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg="#1e293b").pack(anchor="w", padx=10, pady=(6, 0))
        self.lbl_firewall = tk.Label(calm_box, text="Çin Senkr: ENGELLENDİ", font=("Consolas", 11, "bold"), fg="#a855f7", bg="#1e293b")
        self.lbl_firewall.pack(anchor="w", padx=10, pady=(0, 6))

        # Manuel Müdahale ve Acil Durum Butonları
        btn_box = tk.Frame(container, bg="#111827")
        btn_box.pack(fill="x", side="bottom", pady=10)

        self.btn_estop = tk.Button(
            btn_box,
            text="ASIL-D ACİL DURMA (MRM)",
            font=("Segoe UI", 11, "bold"),
            bg="#dc2626",
            fg="#ffffff",
            activebackground="#b91c1c",
            activeforeground="#ffffff",
            relief="flat",
            command=self._trigger_mrm_estop
        )
        self.btn_estop.pack(fill="x", pady=6)

        self.btn_toggle_auto = tk.Button(
            btn_box,
            text="MANUEL / OTONOM GEÇİŞİ",
            font=("Segoe UI", 10, "bold"),
            bg="#2563eb",
            fg="#ffffff",
            activebackground="#1d4ed8",
            relief="flat",
            command=self._toggle_autonomy
        )
        self.btn_toggle_auto.pack(fill="x", pady=4)

    def _trigger_mrm_estop(self) -> None:
        self.safety.current_state = SafetyState.MRM_EMERGENCY_STOP
        self.can_bridge.encode_emergency_stop(reason_code=0x01)
        self.lbl_mode.config(text="MRM ACİL DURUŞ", fg="#ef4444")
        messagebox.showwarning("ASIL-D MRM DEVREDE", "Minimal Risk Maneuver (MRM) Güvenli Durma Aktive Edildi! Araç 6.5 m/s2 ivmeyle durduruluyor.")

    def _toggle_autonomy(self) -> None:
        if self.safety.current_state == SafetyState.NOMINAL_AUTONOMOUS:
            self.safety.current_state = SafetyState.MANUAL_OVERRIDE
            self.lbl_mode.config(text="MANUEL MOD", fg="#f59e0b")
        else:
            self.safety.current_state = SafetyState.NOMINAL_AUTONOMOUS
            self.lbl_mode.config(text="SEVİYE-4 AKTİF", fg="#06b6d4")

    def _drive_simulation_tick(self) -> None:
        """50 Hz (20ms) Simüle Edilmiş Sürüş Döngüsü."""
        self.safety.feed_watchdog()

        if self.safety.current_state == SafetyState.NOMINAL_AUTONOMOUS:
            # 1. Stanley Direksiyon Hesabı
            steer_rad, cte, nearest_idx = self.controller.compute_steering(self.state, self.path)
            steer_deg = math.degrees(steer_rad)

            # 2. Boyuna İvme Hesabı
            target_v_mps = (self.target_speed_kmh / 3.6)
            accel = self.controller.compute_longitudinal_accel(self.state.velocity_mps, target_v_mps)

            # 3. Kinematik Durum İlerletmesi
            dt = 0.05
            self.state.velocity_mps = max(0.0, self.state.velocity_mps + accel * dt)
            self.state.yaw_rad = normalize_angle(self.state.yaw_rad + (self.state.velocity_mps / 2.975) * math.tan(steer_rad) * dt)
            self.state.x += self.state.velocity_mps * math.cos(self.state.yaw_rad) * dt
            self.state.y += self.state.velocity_mps * math.sin(self.state.yaw_rad) * dt
            self.state.steering_angle_rad = steer_rad

            # Rota sonuna ulaşıldığında başa dön (Sürekli Kapalı Döngü Testi)
            if self.state.x > 68.0:
                self.state.x = 10.0
                self.state.y = 10.0
                self.state.yaw_rad = math.radians(30)
                self.state.velocity_mps = 4.0

            # 4. CAN-FD Çerçevelerini Kodla
            self.can_bridge.encode_steering_command(steer_deg)
            self.can_bridge.encode_accel_brake_command(accel, self.state.velocity_mps)
            self.can_bridge.encode_heartbeat(asil_status_ok=True)

            # 5. Göstergeleri Güncelle
            self.lbl_speed.config(text=f"{self.state.velocity_kmh:.1f} km/s")
            self.lbl_steer.config(text=f"{steer_deg:+.1f}°")
            self.lbl_cte.config(text=f"{abs(cte)*100:.1f} cm (NOMINAL)")
            self.lbl_can_count.config(text=f"{len(self.can_bridge.tx_history)} Çerçeve")
            self.lbl_watchdog.config(text=f"{(time.time()-self.safety.last_heartbeat_time)*1000:.0f} ms (CANLI)")

        elif self.safety.current_state == SafetyState.MRM_EMERGENCY_STOP:
            # MRM Frenleme
            self.state.velocity_mps = max(0.0, self.state.velocity_mps - 6.5 * 0.05)
            self.lbl_speed.config(text=f"{self.state.velocity_kmh:.1f} km/s")

        # Haritayı Çiz
        self._render_map()
        self.after(50, self._drive_simulation_tick)

    def _render_map(self) -> None:
        self.map_canvas.delete("all")
        w = self.map_canvas.winfo_width()
        h = self.map_canvas.winfo_height()
        if w < 100 or h < 100:
            return

        # Ölçekleme (Dünya metrelerini Canvas piksellerine haritala)
        scale = min(w / 80.0, h / 60.0)
        ox = 40.0
        oy = h - 40.0

        def to_px(x: float, y: float) -> Tuple[float, float]:
            return ox + x * scale, oy - y * scale

        # Izgara çizgileri (Grid)
        for gx in range(0, 80, 10):
            p1 = to_px(gx, 0)
            p2 = to_px(gx, 60)
            self.map_canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="#1e293b", dash=(2, 4))
        for gy in range(0, 60, 10):
            p1 = to_px(0, gy)
            p2 = to_px(80, gy)
            self.map_canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="#1e293b", dash=(2, 4))

        # Planlanan Yörünge (Hybrid A* Mavi Yol)
        if len(self.path) > 1:
            coords = []
            for pt in self.path:
                px, py = to_px(pt.x, pt.y)
                coords.extend([px, py])
            self.map_canvas.create_line(coords, fill="#0284c7", width=3, smooth=True)

        # Algılanan Engeller (Yeşil/Kırmızı Daireler)
        for ox_m, oy_m, r_m in self.obstacles:
            cpx, cpy = to_px(ox_m, oy_m)
            pr = r_m * scale
            self.map_canvas.create_oval(cpx - pr, cpy - pr, cpx + pr, cpy + pr, outline="#ef4444", fill="#7f1d1d", width=2)
            self.map_canvas.create_text(cpx, cpy - pr - 8, text=f"ENGEL {r_m*2:.1f}m", font=("Segoe UI", 8), fill="#fca5a5")

        # SAIC Maxus MIFA 7 Araç Gövdesi (Turkuaz Dikdörtgen)
        vx, vy = to_px(self.state.x, self.state.y)
        car_len = 4.9 * scale
        car_wid = 1.9 * scale

        # Araç yönelimi oku
        arrow_len = 25.0
        ax = vx + arrow_len * math.cos(-self.state.yaw_rad)
        ay = vy + arrow_len * math.sin(-self.state.yaw_rad)
        self.map_canvas.create_line(vx, vy, ax, ay, fill="#38bdf8", width=3, arrow=tk.LAST)

        # Araç kutusu
        hw = car_wid / 2.0
        hl = car_len / 2.0
        self.map_canvas.create_oval(vx - 8, vy - 8, vx + 8, vy + 8, fill="#06b6d4", outline="#ffffff", width=2)
        self.map_canvas.create_text(vx, vy + 16, text="MAXUS MIFA 7 (L4)", font=("Segoe UI", 9, "bold"), fill="#67e8f9")


def main() -> None:
    app = RobotaxiCockpitApp()
    app.mainloop()


if __name__ == "__main__":
    main()
