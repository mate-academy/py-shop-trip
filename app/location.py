from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass
class Location:
    x_coord: int
    y_coord: int

    def __eq__(self, other: Location) -> bool:
        if isinstance(other, Location):
            return (self.x_coord == other.x_coord
                    and self.y_coord == other.y_coord)
        return False

    def distance_to_location(self, other: Location) -> int | float:
        ac = other.x_coord - self.x_coord
        bc = other.y_coord - self.y_coord
        distance = sqrt(ac ** 2 + bc ** 2)
        return distance


def create_location_from_list(coordinates: list) -> Location:
    return Location(
        coordinates[0],
        coordinates[1]
    )
