"""
TRUSTIA Gerçek Zamanlı Telemetri ve API Sunucusu (Sistem 6 / Sistem 3).

Saha Operatörleri ve Taktik Web Konsolu İçin:
  * Canlı Araç Telemetrisi (Konum, Hız, Batarya, SLAM Güveni, Tehdit İzolasyonu)
  * REST / JSON-RPC / WebSocket uyumlu hafif veri akışı
  * Sıfır dış bağımlılık (saf standart kütüphane HTTP/Socket motoru)
"""

from __future__ import annotations

import json
import threading
import time
from dataclasses import asdict, dataclass, field
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict, List, Optional


@dataclass
class VehicleTelemetrySnapshot:
    """Tek bir araç telemetri anlık görüntüsü."""
    vehicle_id: str = "IKA-ALPHA"
    timestamp_s: float = field(default_factory=time.time)
    east_m: float = 0.0
    north_m: float = 0.0
    speed_mps: float = 0.0
    heading_deg: float = 0.0
    battery_pct: float = 100.0
    estop_active: bool = False
    active_threats_count: int = 0
    slam_status: str = "GPS_DENIED_ACTIVE"
    mode: str = "AUTONOMOUS"


class TelemetryDataHub:
    """Tüm araçlardan gelen telemetriyi toplayan ve dağıtan merkezi havuz."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._telemetry: Dict[str, VehicleTelemetrySnapshot] = {}

    def update_telemetry(self, snapshot: VehicleTelemetrySnapshot) -> None:
        with self._lock:
            self._telemetry[snapshot.vehicle_id] = snapshot

    def get_snapshot(self, vehicle_id: str = "IKA-ALPHA") -> Optional[Dict[str, Any]]:
        with self._lock:
            snap = self._telemetry.get(vehicle_id)
            return asdict(snap) if snap else None

    def get_all_snapshots(self) -> Dict[str, Any]:
        with self._lock:
            return {k: asdict(v) for k, v in self._telemetry.items()}


class _TelemetryHttpHandler(BaseHTTPRequestHandler):
    """Hafif JSON Telemetri HTTP İşleyicisi."""

    hub: TelemetryDataHub = TelemetryDataHub()

    def do_GET(self) -> None:
        if self.path in ("/api/telemetry", "/telemetry", "/"):
            data = self.hub.get_all_snapshots()
            resp = json.dumps({"status": "OK", "timestamp": time.time(), "fleet": data}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(resp)))
            self.end_headers()
            self.wfile.write(resp)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format: str, *args: Any) -> None:
        # Sessiz log
        pass


class TelemetryStreamServer:
    """Arka planda çalışan canlı telemetri yayın sunucusu."""

    def __init__(self, host: str = "127.0.0.1", port: int = 8090) -> None:
        self.host = host
        self.port = port
        self.hub = TelemetryDataHub()
        self._server: Optional[HTTPServer] = None
        self._thread: Optional[threading.Thread] = None
        self.is_running = False

    def start(self) -> None:
        if self.is_running:
            return
        _TelemetryHttpHandler.hub = self.hub
        try:
            self._server = HTTPServer((self.host, self.port), _TelemetryHttpHandler)
            self.is_running = True
            self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
            self._thread.start()
        except OSError:
            self.is_running = False

    def stop(self) -> None:
        if self._server:
            self._server.shutdown()
            self._server.server_close()
            self._server = None
        self.is_running = False
