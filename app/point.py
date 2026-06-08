import math


class Point:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = x_coord
        self.y = y_coord

    def distance_to_point(self, point: "Point") -> int | float :
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
