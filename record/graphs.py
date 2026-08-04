"""
TRUSTIA Veri Kayıt (Sistem 4) — Telemetri grafikleri.

Bağımlılıksız (saf stdlib) SVG üretici: telemetri çizgi serileri ve
dünya plan görünümü (rota izi) raporlara kanıt dosyası olarak gömülür.
"""

from __future__ import annotations

import html
import os
from typing import Dict, List, Optional, Sequence, Tuple


def _clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


def _axis(values: Sequence[float], lo: Optional[float], hi: Optional[float]):
    if not values:
        return 0.0, 1.0
    data_lo = min(values) if lo is None else lo
    data_hi = max(values) if hi is None else hi
    if data_hi - data_lo < 1e-9:
        data_hi = data_lo + 1.0
    return data_lo, data_hi


def line_svg(
    path: str,
    x_values: Sequence[float],
    series: Dict[str, Sequence[float]],
    title: str = "",
    y_label: str = "",
    y_lo: Optional[float] = None,
    y_hi: Optional[float] = None,
    width: int = 700,
    height: int = 240,
    colors: Sequence[str] = ("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"),
) -> str:
    """Çizgi grafiğini SVG dosyasına yazar; dosya yolu döndürülür."""
    margin_l, margin_r, margin_t, margin_b = 46, 12, 14, 26
    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b
    domain = (0.0, float(max(x_values)) if x_values else 1.0)
    if domain[1] <= domain[0]:
        domain = (0.0, 1.0)
    data_lo, data_hi = _axis(
        [v for s in series.values() for v in s], y_lo, y_hi
    )

    def sx(x: float) -> float:
        return margin_l + (x - domain[0]) / (domain[1] - domain[0]) * plot_w

    def sy(y: float) -> float:
        return margin_t + (1.0 - (y - data_lo) / (data_hi - data_lo)) * plot_h

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}">',
        "<rect width=\"100%\" height=\"100%\" fill=\"#ffffff\"/>",
    ]
    if title:
        lines.append(
            f'<text x="{width / 2}" y="12" font-size="12" '
            f'font-family="sans-serif" text-anchor="middle" '
            f'font-weight="bold">{html.escape(title)}</text>'
        )
    # ızgara + y ekseni etiketleri
    for i in range(5):
        ratio = i / 4.0
        gy = margin_t + (1.0 - ratio) * plot_h
        value = data_lo + ratio * (data_hi - data_lo)
        lines.append(
            f'<line x1="{margin_l}" y1="{gy:.1f}" x2="{width - margin_r}" '
            f'y2="{gy:.1f}" stroke="#e0e0e0" stroke-width="0.5"/>'
        )
        lines.append(
            f'<text x="{margin_l - 4}" y="{gy + 3:.1f}" font-size="9" '
            f'font-family="sans-serif" text-anchor="end">'
            f'{value:.2f}</text>'
        )
    lines.append(
        f'<line x1="{margin_l}" y1="{margin_t}" x2="{margin_l}" '
        f'y2="{height - margin_b}" stroke="#555" stroke-width="1"/>'
    )
    lines.append(
        f'<line x1="{margin_l}" y1="{height - margin_b}" '
        f'x2="{width - margin_r}" y2="{height - margin_b}" '
        f'stroke="#555" stroke-width="1"/>'
    )
    if y_label:
        lines.append(
            f'<text x="10" y="{margin_t + 8}" font-size="9" '
            f'font-family="sans-serif" fill="#666">{html.escape(y_label)}</text>'
        )
    for index, (label, values) in enumerate(series.items()):
        color = colors[index % len(colors)]
        if len(values) != len(x_values) or not values:
            continue
        points = [
            f"{sx(x):.1f},{sy(y):.1f}"
            for x, y in zip(x_values, values)
        ]
        lines.append(
            f'<polyline points="{" ".join(points)}" fill="none" '
            f'stroke="{color}" stroke-width="1.5"/>'
        )
    # lejant
    ly = margin_t + 2
    for index, label in enumerate(series):
        color = colors[index % len(colors)]
        lines.append(
            f'<rect x="{width - 170}" y="{ly + index * 12}" width="10" '
            f'height="10" fill="{color}"/>'
        )
        lines.append(
            f'<text x="{width - 156}" y="{ly + index * 12 + 9}" font-size="9">'
            f'{html.escape(label)}</text>'
        )
    lines.append("</svg>")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    return path


def trajectory_svg(
    path: str,
    points: Sequence[Tuple[float, float]],
    world_size_m: float,
    obstacles: Sequence[Tuple[float, float, float]] = (),
    title: str = "Rota İzi (üstten görünüm)",
    width: int = 700,
    height: int = 560,
) -> str:
    """Dünya plan görünümü: araç izi + engeller."""
    margin = 24
    plot_w = width - 2 * margin
    plot_h = height - 2 * margin

    def sx(x: float) -> float:
        return margin + x / world_size_m * plot_w

    def sy(y: float) -> float:
        return margin + (world_size_m - y) / world_size_m * plot_h

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fbfbfb"/>',
        '<rect width="100%" height="100%" fill="none" stroke="#555" '
        'stroke-width="1"/>',
    ]
    # kılavuz ızgara (her 5 m)
    for i in range(0, int(world_size_m) + 1, 5):
        lines.append(
            f'<line x1="{sx(i):.1f}" y1="{margin}" x2="{sx(i):.1f}" '
            f'y2="{height - margin}" stroke="#e8e8e8" stroke-width="0.5"/>'
        )
        lines.append(
            f'<line x1="{margin}" y1="{sy(i):.1f}" x2="{width - margin}" '
            f'y2="{sy(i):.1f}" stroke="#e8e8e8" stroke-width="0.5"/>'
        )
    for (cx, cy, radius) in obstacles:
        lines.append(
            f'<circle cx="{sx(cx):.1f}" cy="{sy(cy):.1f}" r="{radius * 40:.1f}" '
            f'fill="#e74c3c" fill-opacity="0.55"/>'
        )
    if len(points) > 1:
        trail = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in points)
        lines.append(
            f'<polyline points="{trail}" fill="none" stroke="#1f77b4" '
            f'stroke-width="2"/>'
        )
    if points:
        x0, y0 = points[0]
        xt, yt = points[-1]
        lines.append(
            f'<circle cx="{sx(x0):.1f}" cy="{sy(y0):.1f}" r="5" '
            f'fill="#2ca02c" stroke="#fff"/>'
        )
        lines.append(
            f'<circle cx="{sx(xt):.1f}" cy="{sy(yt):.1f}" r="5" '
            f'fill="#9467bd" stroke="#fff"/>'
        )
    if title:
        lines.append(
            f'<text x="{width / 2}" y="12" font-size="12" '
            f'font-family="sans-serif" text-anchor="middle" '
            f'font-weight="bold">{html.escape(title)}</text>'
        )
    lines.append("</svg>")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    return path


def export_mission_charts(
    directory: str,
    base_name: str,
    steps: Sequence[int],
    positions: Sequence[Tuple[float, float]],
    world_size_m: float,
    obstacles: Sequence[Tuple[float, float, float]] = (),
    speed: Optional[Sequence[float]] = None,
    battery: Optional[Sequence[float]] = None,
    link: Optional[Sequence[float]] = None,
    error: Optional[Sequence[float]] = None,
) -> List[str]:
    """Görev grafiklerini zincir halinde üretir; üretilen yolları döndürür."""
    paths: List[str] = []
    if speed is not None and battery is not None and link is not None:
        paths.append(line_svg(
            os.path.join(directory, f"{base_name}_telemetry.svg"),
            steps, {"hız (m/s)": speed, "batarya (%)": battery, "bağlantı": link},
            title="Telemetri — hız, batarya, bağlantı",
            y_label="değer",
            y_lo=0.0, y_hi=100.0,
        ))
    if error is not None:
        paths.append(line_svg(
            os.path.join(directory, f"{base_name}_error.svg"),
            steps, {"konum hatası (m)": error},
            title="GPS'siz konum hatası",
            y_label="hata (m)",
        ))
    paths.append(trajectory_svg(
        os.path.join(directory, f"{base_name}_trail.svg"),
        positions, world_size_m=world_size_m, obstacles=obstacles,
    ))
    return paths