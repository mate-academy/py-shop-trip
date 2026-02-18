import math
from typing import Any


def calc_distance(p1: list[int], p2: list[int]) -> float:
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def fmt_money(value: float) -> str:
    formatted_value = f"{value:.2f}"
    formatted_value = formatted_value.rstrip("0").rstrip(".")
    return formatted_value


def require_keys(data: dict[str, Any], keys: list[str]) -> None:
    for key in keys:
        if key not in data:
            raise ValueError(f"{key} is missing in config")
