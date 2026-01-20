import dataclasses
import math

from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    products: dict[str, int]
    location: list[int]
    money: int
    car: Car

    def calculate_distance(self, shop: Shop) -> int | float:
        distance = math.dist(shop.location, self.location)
        return distance
