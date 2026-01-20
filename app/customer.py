from __future__ import annotations
import dataclasses
from decimal import Decimal

from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: Decimal
    car: Car

    def calculate_ride_cost_to(
            self, location: list[int], fuel_price: Decimal
    ) -> Decimal:
        return (
            Decimal(self.car.fuel_consumption) / 100
            * Decimal(self._calculate_distance(location)) * fuel_price
        )

    def _calculate_distance(self, other_location: list[int]) -> int:
        return (
            (self.location[0] - other_location[0]) ** 2
            + (self.location[1] - other_location[1]) ** 2
        ) ** 0.5

    def go_to(self, location: list[int]) -> None:
        self.location = location

    def count_remaining_money(self, trip_cost: Decimal) -> None:
        self.money -= trip_cost

    @staticmethod
    def from_dict(customer_dict: dict) -> Customer:
        return Customer(
            customer_dict["name"],
            customer_dict["product_cart"],
            customer_dict["location"],
            Decimal(customer_dict["money"]),
            Car.from_dict(customer_dict["car"])
        )
