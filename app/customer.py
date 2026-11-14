from __future__ import annotations

from dataclasses import dataclass, field

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: float
    car: Car

    home_location: list[int] = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = self.location.copy()

    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        data = data.copy()
        data["car"] = Car(**data["car"])
        return cls(**data)

    def distance_to_shop(self, shop: Shop) -> float:
        return (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> tuple:
        product_costs, products_total = shop.calculate_products_cost(
            self.product_cart
        )

        fuel_cost = 2 * self.car.calculate_fuel_cost(
            self.distance_to_shop(shop),
            fuel_price,
        )

        trip_cost = fuel_cost + products_total

        return trip_cost, product_costs, products_total

    def go_to_shop(self, shop: Shop, trip_cost: float) -> bool:
        if self.money < trip_cost:
            return False

        self.money -= trip_cost
        self.location = shop.location.copy()
        return True

    def go_home(self) -> None:
        self.location = self.home_location.copy()
