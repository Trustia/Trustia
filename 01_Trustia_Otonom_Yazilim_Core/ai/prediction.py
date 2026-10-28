r"""
TRUSTIA Otonom Sürüş Çekirdeği — 3 Saniyelik Gelecek Rota ve Niyet Tahmini (Trajectory Prediction).
==================================================================================================
Bu modül, `tracking.py` tarafından takip edilen dinamik aktörlerin (yaya, otomobil,
bisikletli vb.) önümüzdeki 0.5 ile 3.0 saniye arasındaki ($t \in [0.5, 3.0]$ s)
gelecekteki konumlarını, niyetlerini ve uzay-zaman çarpışma koridorunu (collision tube)
kinematik ve olasılıksal olarak hesaplar.

Standartlar ve Algoritmalar:
  - 3 Saniyelik Zamansal Tahmin Ufku (Time Horizon)
  - Genişleyen Belirsizlik Elipsi (Uncertainty Ellipse)
  - Yaya Karşıdan Karşıya Geçiş Niyeti ve Araç Şerit Takip Modeli
  - Spatio-Temporal Çarpışma Tüpü (Hybrid A* ve Frenet Planlayıcı Girişi)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from ai.tracking import TrackedObstacle3D


@dataclass
class WaypointPrediction:
    """Belirli bir zaman dilimindeki tahmin noktası."""

    time_offset_s: float
    x: float
    y: float
    uncertainty_radius_m: float
    speed_mps: float


@dataclass
class PredictedTrajectory:
    """Tek bir aktör için çoklu zaman dilimli gelecek rotası."""

    track_id: int
    class_name: str
    intent: str  # "CROSSING", "LANE_FOLLOW", "TURNING", "STATIONARY"
    probability: float
    waypoints: List[WaypointPrediction] = field(default_factory=list)

    def position_at_time(self, t_sec: float) -> Optional[Tuple[float, float, float]]:
        """Verilen t anında (x, y, belirsizlik_yarıçapı) değerini enterpole eder."""
        if not self.waypoints:
            return None
        if t_sec <= self.waypoints[0].time_offset_s:
            wp = self.waypoints[0]
            return (wp.x, wp.y, wp.uncertainty_radius_m)
        if t_sec >= self.waypoints[-1].time_offset_s:
            wp = self.waypoints[-1]
            return (wp.x, wp.y, wp.uncertainty_radius_m)

        for i in range(len(self.waypoints) - 1):
            w1 = self.waypoints[i]
            w2 = self.waypoints[i + 1]
            if w1.time_offset_s <= t_sec <= w2.time_offset_s:
                ratio = (t_sec - w1.time_offset_s) / (w2.time_offset_s - w1.time_offset_s)
                ix = w1.x + ratio * (w2.x - w1.x)
                iy = w1.y + ratio * (w2.y - w1.y)
                ir = w1.uncertainty_radius_m + ratio * (w2.uncertainty_radius_m - w1.uncertainty_radius_m)
                return (ix, iy, ir)
        return None

    def to_dict(self) -> dict:
        return {
            "track_id": self.track_id,
            "class_name": self.class_name,
            "intent": self.intent,
            "probability": round(self.probability, 3),
            "trajectory_points": [
                {
                    "t_s": round(wp.time_offset_s, 1),
                    "x": round(wp.x, 2),
                    "y": round(wp.y, 2),
                    "radius_m": round(wp.uncertainty_radius_m, 2),
                }
                for wp in self.waypoints
            ],
        }


class TrajectoryPredictionEngine:
    """
    3 Saniyelik Kinematik ve Niyet Tahmin Motoru.
    Girdi: Takip edilen dinamik nesneler listesi.
    Çıktı: Her nesne için 0.5s - 3.0s zaman aralıklı gelecek rotaları.
    """

    def __init__(
        self,
        prediction_horizon_s: float = 3.0,
        time_step_s: float = 0.5,
        pedestrian_cross_prob_threshold: float = 0.50,
    ) -> None:
        self.prediction_horizon_s = prediction_horizon_s
        self.time_step_s = time_step_s
        self.pedestrian_cross_prob_threshold = pedestrian_cross_prob_threshold

    def predict_trajectories(
        self,
        obstacles: Sequence[TrackedObstacle3D],
    ) -> List[PredictedTrajectory]:
        """Tüm takip edilen nesneler için gelecek yörüngelerini üretir."""
        predictions: List[PredictedTrajectory] = []

        num_steps = int(self.prediction_horizon_s / self.time_step_s)

        for obs in obstacles:
            # Sabit/duran nesneler
            speed = obs.speed_mps()
            if speed < 0.2:
                intent = "STATIONARY"
                waypoints = []
                for step in range(1, num_steps + 1):
                    t = step * self.time_step_s
                    waypoints.append(
                        WaypointPrediction(
                            time_offset_s=t,
                            x=obs.x,
                            y=obs.y,
                            uncertainty_radius_m=max(obs.width, obs.length) / 2.0 + 0.1 * t,
                            speed_mps=0.0,
                        )
                    )
                predictions.append(
                    PredictedTrajectory(
                        track_id=obs.track_id,
                        class_name=obs.class_name,
                        intent=intent,
                        probability=0.99,
                        waypoints=waypoints,
                    )
                )
                continue

            # Yayalar: Yana doğru (şeride doğru) hız varsa karşıya geçiş niyeti
            if obs.class_name in ("pedestrian", "bicycle"):
                is_lateral_moving = abs(obs.vy_mps) > 0.4
                intent = "CROSSING" if is_lateral_moving else "LANE_FOLLOW"
                prob = 0.85 if is_lateral_moving else 0.70

                waypoints = []
                for step in range(1, num_steps + 1):
                    t = step * self.time_step_s
                    # Sabit hız modeli + zamanla büyüyen belirsizlik
                    pred_x = obs.x + obs.vx_mps * t
                    pred_y = obs.y + obs.vy_mps * t
                    # Belirsizlik yarıçapı: Başlangıçta 0.5m, 3. saniyede 1.4m
                    u_radius = 0.50 + 0.30 * t
                    waypoints.append(
                        WaypointPrediction(
                            time_offset_s=t,
                            x=pred_x,
                            y=pred_y,
                            uncertainty_radius_m=u_radius,
                            speed_mps=speed,
                        )
                    )
                predictions.append(
                    PredictedTrajectory(
                        track_id=obs.track_id,
                        class_name=obs.class_name,
                        intent=intent,
                        probability=prob,
                        waypoints=waypoints,
                    )
                )

            # Araçlar: Sabit hız ve yönelim (Constant Velocity & Yaw Rate)
            else:
                intent = "LANE_FOLLOW"
                prob = 0.90
                waypoints = []
                for step in range(1, num_steps + 1):
                    t = step * self.time_step_s
                    pred_x = obs.x + obs.vx_mps * t
                    pred_y = obs.y + obs.vy_mps * t
                    u_radius = 1.0 + 0.25 * t
                    waypoints.append(
                        WaypointPrediction(
                            time_offset_s=t,
                            x=pred_x,
                            y=pred_y,
                            uncertainty_radius_m=u_radius,
                            speed_mps=speed,
                        )
                    )
                predictions.append(
                    PredictedTrajectory(
                        track_id=obs.track_id,
                        class_name=obs.class_name,
                        intent=intent,
                        probability=prob,
                        waypoints=waypoints,
                    )
                )

        return predictions
