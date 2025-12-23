import math

from dataclasses import dataclass, field
from typing import List, Dict, Any

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    money: int
    car: Car
    product_cart: Dict[str, int]
    location: List[float]
    home_location: List[float] = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = self.location.copy()

    def calculate_distance(self, point: List[float]) -> float:

        return math.sqrt((self.location[0]
                          - point[0]) ** 2 + (self.location[1]
                                              - point[1]) ** 2)

    def trip_cost(
            self,
            shop: "Shop",
            fuel_price: float) -> tuple[int, dict[str, Any], int]:
        total_travel_distance = self.calculate_distance(shop.location) * 2

        total_fuel_cost = self.car.calculate_fuel_cost(
            total_travel_distance, fuel_price
        )

        (product_cost,
         purchase_info) = shop.calculate_purchase_cost(
            self.product_cart
        )

        total_cost = total_fuel_cost + product_cost

        return round(total_cost, 2), purchase_info, product_cost

    def move_to_shop(self, shop: "Shop") -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location.copy()

    def move_to_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location.copy()

    def make_purchase(
            self,
            shop: "Shop",
            purchase_cost: int,
            purchase_details: Dict[str, Any]
    ) -> None:

        self.money -= purchase_cost
        shop.print_receipt(self.name, purchase_details, purchase_cost)
