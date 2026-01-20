from __future__ import annotations
from decimal import Decimal
from dataclasses import dataclass

from .car import Car
from .shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: Decimal
    car: Car

    @classmethod
    def from_dict(cls, dict_: dict) -> Customer:
        return cls(
            name=dict_["name"],
            product_cart=dict_["product_cart"],
            location=dict_["location"],
            money=Decimal.from_float(dict_["money"]),
            car=Car.from_dict(dict_["car"]),
        )

    def get_distance(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def get_trip_cost(self, shop: Shop, fuel_price: Decimal) -> Decimal:
        distance = self.get_distance(shop)
        return (
            Decimal.from_float(distance / 100 * self.car.fuel_consumption)
            * fuel_price
        )

    def get_full_trip_cost(self, shop: Shop, fuel_price: Decimal) -> Decimal:
        return self.get_trip_cost(shop, fuel_price) * 2 + sum(
            shop.get_products_costs(self.product_cart).values()
        )

    def visit_shop(self, shop: Shop, fuel_price: Decimal) -> None:
        print(f"{self.name} rides to {shop.name}\n")

        trip_cost = self.get_trip_cost(shop, fuel_price)

        home_location = self.location
        self.location = shop.location
        self.money -= trip_cost

        shop.serve_customer(self)
        print()

        print(f"{self.name} rides home")
        self.location = home_location
        self.money -= trip_cost
