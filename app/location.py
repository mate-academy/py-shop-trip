from dataclasses import dataclass
from math import sqrt


@dataclass
class Location:
    x_coord: int
    y_coord: int

    def distance(self, other: Location) -> float:
        return sqrt((other.x_coord - self.x_coord) ** 2
                    + (other.y_coord - self.y_coord) ** 2)
