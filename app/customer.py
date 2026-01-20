from dataclasses import dataclass
from app.car import Car
from app.shop import Shop
import math


@dataclass
class Customer:
    name: str
    product_cart: dict[str, float]
    location: list[int]
    money: int
    car: Car

    def __init__(self, **kwargs) -> None:
        kwargs["car"] = Car(**kwargs["car"])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def spend_money(self, expenses: float) -> None:
        self.money -= expenses

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        return (
            self.get_products_expense(shop)
            + self.get_fuel_expense(shop, fuel_price)
        )

    def get_fuel_expense(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(shop.location, self.location)
        return round(
            distance / 100 * self.car.fuel_consumption * fuel_price * 2,
            2
        )

    def get_products_expense(self, shop: Shop) -> float:
        return sum(
            self.product_cart[key] * shop.products[key]
            for key in self.product_cart
        )
