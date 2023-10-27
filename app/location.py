from __future__ import annotations


class Location:
    def __init__(self, coordinate: list[int]) -> None:
        self.latitude = coordinate[0]
        self.longitude = coordinate[1]

    def calculate_distance(self, other: Location) -> float:
        distance = (
            (other.longitude - self.longitude) ** 2
            + (other.latitude - self.latitude) ** 2
        ) ** 0.5
        return distance
