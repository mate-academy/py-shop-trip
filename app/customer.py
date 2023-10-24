from dataclasses import dataclass
from typing import List
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: float
    car: Car
    shop_info: List[list]

    def get_track_distance(self, shop_location: list) -> float:
        distance_x = self.location[0] - shop_location[0]
        distance_y = self.location[1] - shop_location[1]
        return (distance_x ** 2 + distance_y ** 2) ** 0.5 * 2
