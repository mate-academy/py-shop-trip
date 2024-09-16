import math


class Location:
    def __init__(self, location: dict):
        self.x = location[0]
        self.y = location[1]

    def calc_distance(self, other) -> float:
        diff_x = other.x - self.x
        diff_y = other.y - self.y
        return math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
