from dataclasses import dataclass
from typing import Dict, List
from math import sqrt
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[float]
    money: float
    car: Car

    def calculate_distance(self, shop_location: list[float]) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_fuel_cost(self,
                            distance: float, fuel_price: float) -> float:
        return distance * 2 * self.car.fuel_consumption / 100 * fuel_price

    def calculate_cart_cost(self,
                            shop_products: dict[str, float]) -> float:
        total_car_cost = 0

        for product, quantity in self.product_cart.items():
            total_car_cost += shop_products[product] * quantity

        return total_car_cost
