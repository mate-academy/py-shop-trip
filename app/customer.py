# flake8: noqa
from app.car import Car
from typing import Any
from decimal import Decimal


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int | float],
            money: int | float,
            car: dict) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = Decimal(str(money))
        self.car = Car(
            brand=car.get("brand"),
            fuel_consumption=car.get("fuel_consumption"),
        )

    def go_to_trip(self, shop: Any) -> int | float:
        trip_sum = Decimal("0")
        trip_sum += self.car.ride_to_the_shop(
            self.location,
            shop.location
        ) * Decimal("2")

        shoping_result = shop.buy_products(
            self
        )
        if not shoping_result:
            return f"There aren't requested products in the shop called: {shop.name}"
        return trip_sum + shoping_result
