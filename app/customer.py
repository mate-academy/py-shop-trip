from __future__ import annotations
import dataclasses
import math

from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    def calculate_fuel(
            self,
            home_location: list,
            shop_location: list
    ) -> float:
        shop_distance = math.dist(home_location, shop_location)
        need_fuel = shop_distance * 2 / 100 * self.car.fuel_consumption
        return need_fuel

    def count_purchases(self, shop: dict) -> float:
        milk_cost = self.product_cart["milk"]\
            * shop["milk"]
        bread_cost = self.product_cart["bread"]\
            * shop["bread"]
        butter_cost = self.product_cart["butter"]\
            * shop["butter"]
        return milk_cost + bread_cost + butter_cost
