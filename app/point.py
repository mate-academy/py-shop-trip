import math


class Point:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = x_coord
        self.y = y_coord

    def distance_to_point(self, other: "Point") -> float:
        return math.dist((self.x, self.y), (other.x, other.y))
