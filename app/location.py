from __future__ import annotations

import math
from typing import List


class Location:
    def __init__(self, location: List[int, int]) -> None:
        self.x = location[0]
        self.y = location[1]

    def distance_to(self, other: Location) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
        )
