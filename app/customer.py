from dataclasses import dataclass
import math

from app.car import Car
import app.shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: float | int
    car: Car

    def calculate_trip_cost(self,
                            shop_location: list[int],
                            fuel_price: float
                            ) -> float:
        # розрахунок відстані
        x1, y1 = self.location
        x2, y2 = shop_location
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        res = (self.car.fuel_cost(distance, fuel_price))
        return res

    def can_afford_trip(
            self,
            shop: app.shop.Shop,
            fuel_price: float
    ) -> bool:
        cost_product_cart = shop.calculate_product_cart_cost(self.product_cart)
        cost_fuel = self.calculate_trip_cost(shop.location, fuel_price) * 2

        return (cost_fuel + cost_product_cart) <= self.money
