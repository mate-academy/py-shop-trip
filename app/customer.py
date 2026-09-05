import math

from typing import Any

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict[str, int],
                 location: list[int],
                 money: float | int,
                 car: Car
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location.copy()
        self.money = money
        self.car = Car(**car) if isinstance(car, dict) else car

    def money_print(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_shopping_cost(self, shop: Shop) -> float:
        total_cost = sum(
            shop.products[product] * count
            for product, count in self.product_cart.items()
        )

        return round(total_cost, 2)

    def calculate_arriving_double_cost(self,
                                       shop: Shop,
                                       fuel_cost: float) -> float:
        double_distance = math.sqrt(
            (
                math.pow(self.location[0] - shop.location[0], 2)
                + math.pow(self.location[1] - shop.location[1], 2)
            )
        ) * 2
        return round(
            self.car.calculate_fuel_consumption(double_distance) * fuel_cost
            , 2)

    def calculate_full_trip_cost(self, shop: Shop, fuel_cost: float) -> float:
        return round(
            self.calculate_shopping_cost(shop)
            + self.calculate_arriving_double_cost(shop, fuel_cost)
            , 2)

    def shopping(self, shop: Shop) -> None:
        self.location = shop.location.copy()
        shop.print_purchase_receipt(customer=self)

    def ride_home(self) -> None:
        self.location = self.home_location.copy()
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Customer":
        return cls(**data)
