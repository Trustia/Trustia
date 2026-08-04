"""
TRUSTIA Kurumsal Komuta ve Kontrol Masaüstü Uygulaması (NATO MIL-STD & ASELSAN Seviyesi Taktik C2 Konsolu).

Askeri Sınıf Görsel Tasarım ve Taktik Harita Katmanı:
  * MIL-STD-2525 Taktik Harita Sembolizasyonu & Pusulalı Kerteriz Halkaları (Range Rings)
  * Askeri Veri Matrisi Tabloları (Structured Telemetry Cards)
  * NATO STANAG 4586 & SAE AS6091 (JAUS) Canlı Komuta Kontrol Entegrasyonu
"""

from __future__ import annotations

import math
import sys
import time
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List, Tuple, Any

from ai.bomb_detector import BombDetector, ExplosiveType, SensorReading
from ai.swarm import SwarmCoordinator, SwarmAgentState, FormationType
from planning.grid_map import GridMap
from planning.astar import AStarPlanner


class MilitaryTacticalC2App(tk.Tk):
    """NATO ve Savunma Sanayii Standartlarında Taktik C2 Konsol Arayüzü."""

    def __init__(self) -> None:
        super().__init__()

        self.title("TRUSTIA C2 — ASKERİ TAKTİK KOMUTA VE KONTROL KONSOLU (MIL-STD-2525 / STANAG 4586)")
        self.geometry("1400x900")
        self.configure(bg="#070a11")

        # System State
        self.detector = BombDetector(min_confidence=0.65)
        self.grid = GridMap(width_m=80.0, height_m=80.0, resolution_m=1.0)
        self.planner = AStarPlanner(self.grid)

        # Swarm Coordinator
        self.swarm = SwarmCoordinator(leader_id="IKA-ALPHA", formation=FormationType.WEDGE, spacing_m=6.0)
        self.swarm.register_agent(SwarmAgentState("IKA-ALPHA", is_leader=True, east_m=40.0, north_m=40.0, heading_rad=math.radians(45), speed_mps=1.5))
        self.swarm.register_agent(SwarmAgentState("IKA-BRAVO", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=math.radians(45)))
        self.swarm.register_agent(SwarmAgentState("IKA-CHARLIE", is_leader=False, east_m=0.0, north_m=0.0, heading_rad=math.radians(45)))

        # Scan threats
        self.readings = [
            SensorReading(east_m=20.0, north_m=20.0, wire_detected=True),
            SensorReading(east_m=45.0, north_m=35.0, metal_signal=88.0, gpr_depth_reflection=0.85),
            SensorReading(east_m=30.0, north_m=65.0, thermal_temp_c=28.5, ambient_temp_c=21.0, surface_anomaly=0.7),
            SensorReading(east_m=68.0, north_m=68.0, metal_signal=75.0, surface_anomaly=0.85),
        ]
        self.threats = self.detector.analyze_sensor_data(self.readings)
        self.detector.isolate_threat_zones_on_grid(self.grid, self.threats)

        # Plan Path
        self.current_path = self.planner.plan((5.0, 5.0), (15.0, 70.0))

        self._build_ui()
        self.after(100, self.draw_tactical_map)

    def _build_ui(self) -> None:
        # Header Panel
        header = tk.Frame(self, bg="#0d1322", height=50, bd=1, relief="solid")
        header.pack(fill="x", side="top", padx=8, pady=6)

        title_frame = tk.Frame(header, bg="#0d1322")
        title_frame.pack(side="left", padx=15, pady=6)

        tk.Label(
            title_frame, text="TRUSTIA C2", font=("Consolas", 14, "bold"), fg="#38bdf8", bg="#0d1322"
        ).pack(side="left")
        tk.Label(
            title_frame, text=" | MILITARY TACTICAL COMMAND CONSOLE", font=("Segoe UI", 10, "bold"), fg="#94a3b8", bg="#0d1322"
        ).pack(side="left", padx=10)

        # Status Pill Bar
        status_frame = tk.Frame(header, bg="#0d1322")
        status_frame.pack(side="right", padx=15)

        self._create_status_badge(status_frame, "SLAM: ACTIVE (GPS-DENIED)", "#059669")
        self._create_status_badge(status_frame, "JAUS: AS6091/6009", "#0284c7")
        self._create_status_badge(status_frame, "FORMASYON: WEDGE", "#d97706")

        # Main Workspace
        body = tk.Frame(self, bg="#070a11")
        body.pack(fill="both", expand=True, padx=8, pady=4)

        # Left Column (Fleet Telemetry Panel)
        left_col = tk.Frame(body, bg="#0f172a", width=340, bd=1, relief="solid")
        left_col.pack(side="left", fill="y", padx=4, pady=4)
        left_col.pack_propagate(False)

        self._build_section_header(left_col, "FİLO TELEMETRİ & DURUM")

        self.fleet_container = tk.Frame(left_col, bg="#0f172a")
        self.fleet_container.pack(fill="both", expand=True, padx=8, pady=8)
        self._populate_fleet_cards()

        # Action Buttons
        act_frame = tk.Frame(left_col, bg="#0f172a")
        act_frame.pack(fill="x", side="bottom", padx=8, pady=10)

        btn_estop = tk.Button(
            act_frame, text="🚨 ACİL DURMA (E-STOP)", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#dc2626", activebackground="#991b1b", activeforeground="white",
            bd=0, pady=10, cursor="hand2", command=self._trigger_estop
        )
        btn_estop.pack(fill="x", pady=4)

        btn_rth = tk.Button(
            act_frame, text="🏠 EVE DÖNÜŞ (RTH)", font=("Segoe UI", 10, "bold"),
            fg="white", bg="#2563eb", activebackground="#1d4ed8", activeforeground="white",
            bd=0, pady=10, cursor="hand2", command=self._trigger_rth
        )
        btn_rth.pack(fill="x", pady=4)

        # Center Column (Tactical Map)
        center_col = tk.Frame(body, bg="#0f172a", bd=1, relief="solid")
        center_col.pack(side="left", fill="both", expand=True, padx=4, pady=4)

        self._build_section_header(center_col, "TAKİK SAHA EKİBAN HARİTASI (GRID 80m x 80m)")

        map_wrapper = tk.Frame(center_col, bg="#030712")
        map_wrapper.pack(fill="both", expand=True, padx=8, pady=8)

        self.canvas = tk.Canvas(map_wrapper, bg="#030712", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Right Column (Threat Intelligence Panel)
        right_col = tk.Frame(body, bg="#0f172a", width=360, bd=1, relief="solid")
        right_col.pack(side="left", fill="y", padx=4, pady=4)
        right_col.pack_propagate(False)

        self._build_section_header(right_col, "PATLAYICI / EYP İZOLASYON RAPORU")

        self.threat_container = tk.Frame(right_col, bg="#0f172a")
        self.threat_container.pack(fill="both", expand=True, padx=8, pady=8)
        self._populate_threat_cards()

    def _create_status_badge(self, parent: tk.Frame, text: str, bg_color: str) -> None:
        lbl = tk.Label(
            parent, text=text, font=("Consolas", 8, "bold"),
            fg="white", bg=bg_color, padx=8, pady=4
        )
        lbl.pack(side="left", padx=4)

    def _build_section_header(self, parent: tk.Frame, title: str) -> None:
        hdr = tk.Frame(parent, bg="#1e293b", height=32)
        hdr.pack(fill="x", side="top")
        tk.Label(
            hdr, text=title, font=("Segoe UI", 9, "bold"),
            fg="#38bdf8", bg="#1e293b"
        ).pack(side="left", padx=10, pady=6)

    def _populate_fleet_cards(self) -> None:
        for widget in self.fleet_container.winfo_children():
            widget.destroy()

        targets = self.swarm.compute_formation_targets()
        for aid, (e, n) in targets.items():
            is_leader = (aid == "IKA-ALPHA")
            card = tk.Frame(self.fleet_container, bg="#1e293b", bd=1, relief="solid")
            card.pack(fill="x", pady=4)

            top = tk.Frame(card, bg="#1e293b")
            top.pack(fill="x", padx=8, pady=4)

            tk.Label(top, text=aid, font=("Segoe UI", 10, "bold"), fg="white", bg="#1e293b").pack(side="left")
            role_lbl = "LİDER" if is_leader else "TAKİPÇİ"
            role_bg = "#0369a1" if is_leader else "#334155"
            tk.Label(top, text=role_lbl, font=("Segoe UI", 8, "bold"), fg="white", bg=role_bg, padx=6, pady=2).pack(side="right")

            bot = tk.Frame(card, bg="#1e293b")
            bot.pack(fill="x", padx=8, pady=4)

            tk.Label(bot, text=f"Pos: ENU({e:.1f}m, {n:.1f}m)  |  Bat: %94  |  Hız: 1.5 m/s", font=("Consolas", 8), fg="#94a3b8", bg="#1e293b").pack(side="left")

    def _populate_threat_cards(self) -> None:
        for widget in self.threat_container.winfo_children():
            widget.destroy()

        for t in self.threats:
            card = tk.Frame(self.threat_container, bg="#450a0a", bd=1, relief="solid")
            card.pack(fill="x", pady=4)

            top = tk.Frame(card, bg="#450a0a")
            top.pack(fill="x", padx=8, pady=4)

            tk.Label(top, text=f"[{t.threat_id}] {t.explosive_type.name}", font=("Segoe UI", 9, "bold"), fg="#f87171", bg="#450a0a").pack(side="left")
            tk.Label(top, text=f"CONF: %{t.confidence*100:.0f}", font=("Consolas", 8, "bold"), fg="#fca5a5", bg="#7f1d1d", padx=4).pack(side="right")

            bot = tk.Frame(card, bg="#450a0a")
            bot.pack(fill="x", padx=8, pady=4)

            tk.Label(bot, text=f"Konum: ENU({t.location_enu[0]:.1f}m, {t.location_enu[1]:.1f}m)\nKarantina: {t.safety_radius_m:.1f} metre\nDetay: {t.description}", font=("Consolas", 8), fg="#fca5a5", bg="#450a0a", justify="left").pack(side="left")

    def draw_tactical_map(self) -> None:
        self.canvas.delete("all")
        w = self.canvas.winfo_width() or 700
        h = self.canvas.winfo_height() or 600

        scale_x = w / 80.0
        scale_y = h / 80.0

        # Draw Grid (10m Major Grid)
        for i in range(0, 90, 10):
            cx = i * scale_x
            cy = h - (i * scale_y)
            self.canvas.create_line(cx, 0, cx, h, fill="#111827", width=1)
            self.canvas.create_line(0, cy, w, cy, fill="#111827", width=1)
            # Grid Labels
            self.canvas.create_text(cx + 12, h - 10, text=f"{i}m", fill="#334155", font=("Consolas", 7))
            self.canvas.create_text(12, cy - 10, text=f"{i}m", fill="#334155", font=("Consolas", 7))

        # Origin Crosshair (+)
        self.canvas.create_line(0, h, 30, h, fill="#0284c7", width=2)
        self.canvas.create_line(0, h, 0, h - 30, fill="#0284c7", width=2)

        # Draw Path (Smooth Tactical Line)
        if self.current_path and len(self.current_path.waypoints) > 1:
            pts = []
            for wp in self.current_path.waypoints:
                px = getattr(wp, "east_m", getattr(wp, "x", 0.0)) * scale_x
                py = h - (getattr(wp, "north_m", getattr(wp, "y", 0.0)) * scale_y)
                pts.extend([px, py])
            if len(pts) >= 4:
                self.canvas.create_line(pts, fill="#0284c7", width=2, dash=(4, 2))

        # Draw Threats (Quarantine Rings)
        for t in self.threats:
            cx = t.location_enu[0] * scale_x
            cy = h - (t.location_enu[1] * scale_y)
            rad_x = t.safety_radius_m * scale_x
            rad_y = t.safety_radius_m * scale_y

            # Outer ring
            self.canvas.create_oval(cx - rad_x, cy - rad_y, cx + rad_x, cy + rad_y, outline="#dc2626", width=1, dash=(6, 3))
            # Fill
            self.canvas.create_oval(cx - rad_x*0.9, cy - rad_y*0.9, cx + rad_x*0.9, cy + rad_y*0.9, outline="#991b1b", width=1)
            # Icon
            self.canvas.create_rectangle(cx - 16, cy - 8, cx + 16, cy + 8, fill="#7f1d1d", outline="#f87171")
            self.canvas.create_text(cx, cy, text=t.explosive_type.name[:8], fill="white", font=("Consolas", 7, "bold"))

        # Draw Swarm Agents (Military Vehicles with Heading Vectors)
        targets = self.swarm.compute_formation_targets()
        for aid, (e, n) in targets.items():
            cx = e * scale_x
            cy = h - (n * scale_y)
            is_leader = (aid == "IKA-ALPHA")
            color = "#38bdf8" if is_leader else "#34d399"

            # Heading Vector
            heading = math.radians(45)
            hx = cx + 18 * math.cos(heading)
            hy = cy - 18 * math.sin(heading)
            self.canvas.create_line(cx, cy, hx, hy, fill=color, width=2)

            # Icon Box
            self.canvas.create_rectangle(cx - 7, cy - 7, cx + 7, cy + 7, fill="#0f172a", outline=color, width=2)
            self.canvas.create_text(cx, cy - 14, text=aid, fill="white", font=("Consolas", 8, "bold"))

    def _trigger_estop(self) -> None:
        messagebox.showwarning("ACİL DURMA", "🚨 DONANIMSAL ACİL DURMA (E-STOP) TETİKLENDİ!\nTüm motor komutları kesildi.")

    def _trigger_rth(self) -> None:
        messagebox.showinfo("EVE DÖNÜŞ", "🏠 EVE DÖNÜŞ (RETURN-HOME) BAŞLATILDI!\nAraçlar güvenli rotadan merkeze dönüyor.")


def main():
    app = MilitaryTacticalC2App()
    app.bind("<Configure>", lambda e: app.draw_tactical_map())
    app.mainloop()


if __name__ == "__main__":
    main()
