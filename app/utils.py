import json
from math import sqrt
from pathlib import Path


def load_config() -> json:
    """
    Loads and returns the data from config.json by determining its path
    relative to the calling script (e.g., app/utils.py).
    """
    current_dir = Path(__file__).resolve().parent

    config_path = current_dir / "config.json"

    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def calculate_distance(loc1: list[int], loc2: list[int]) -> float:
    """Calculates the Euclidean distance between two 2D locations."""
    x1, y1 = loc1
    x2, y2 = loc2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
