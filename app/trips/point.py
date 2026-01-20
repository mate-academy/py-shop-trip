# flake8: noqa: VNE001
from __future__ import annotations
import math

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x  #noqa: VNE001
        self.y = y  #noqa: VNE001

    def calculate_distance(self, other: Point) -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
