from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Tuple

Location = Tuple[float, float]


def project_root() -> Path:
    """Return the project root folder (the one containing the 'app' folder)."""
    return Path(__file__).resolve().parent.parent


def resolve_config_path(filename: str = "config.json") -> Path:
    """Find config.json in common locations."""
    root_folder = project_root()

    candidates = (
        Path.cwd() / filename,
        root_folder / filename,
        root_folder / "app" / filename,
        root_folder / "configs" / filename,
        root_folder / "config" / filename,
        root_folder / "data" / filename,
    )

    for candidate in candidates:
        if candidate.exists():
            return candidate

    searched = ", ".join(str(path) for path in candidates)
    raise FileNotFoundError(
        f"Could not find '{filename}'. Looked in: {searched}"
    )


def load_config(filename: str = "config.json") -> Dict[str, Any]:
    """Load JSON configuration from disk."""
    config_path = resolve_config_path(filename)
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def to_location(raw: List[float]) -> Location:
    """Convert [x, y] list into a typed (x, y) tuple."""
    if len(raw) != 2:
        raise ValueError("Location must contain exactly 2 numeric values.")

    x_coord, y_coord = raw
    return float(x_coord), float(y_coord)


def euclidean_distance_km(point_a: Location, point_b: Location) -> float:
    """Compute Euclidean distance between two 2D points."""
    delta_x = point_a[0] - point_b[0]
    delta_y = point_a[1] - point_b[1]
    return math.sqrt(delta_x * delta_x + delta_y * delta_y)


def money_fmt(value: float) -> str:
    """Format money with 2 decimals (used for trip costs and final balance)."""
    return f"{value:.2f}"


def money_trim(value: float) -> str:
    """
    Format money without trailing zeros.

    Examples:
    55.0 -> "55"
    12.5 -> "12.5"
    26.50 -> "26.5"
    """
    text = f"{value:.2f}"
    text = text.rstrip("0").rstrip(".")
    return text
