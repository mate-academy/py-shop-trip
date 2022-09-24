import dataclasses
from typing import List

from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: Car

    def distance_to(self, location: List[int]):
        x_distance_square = (self.location[0] - location[0]) ** 2
        y_distance_square = (self.location[1] - location[1]) ** 2
        distance = (x_distance_square + y_distance_square) ** 0.5
        return distance

    def go_to_shop(self, shop):
        self.home = self.location
        print(f"{self.name} rides to {self.shop_to_go.name}\n")
        self.car.make_trip_to(self, shop.location)

        shop.sell_products(self)

    def go_home(self):
        print(f"{self.name} rides home")
        self.car.make_trip_to(self, self.home)
        self.money -= self.trip_price_for_current_shopping
