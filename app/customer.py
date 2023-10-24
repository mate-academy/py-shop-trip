from typing import List
import math
from app import parsing
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            location: List[int],
            money: float,
            product_cart: dict,
            car: Car
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def calculate_fuel_cost(self, car: Car, shop: Shop) -> float:
        fuel_price = parsing.parse_data_from_json()["FUEL_PRICE"]
        distance = math.sqrt((shop.location[0] - self.location[0]) ** 2
                             + (shop.location[1] - self.location[1]) ** 2)
        fuel_cost = fuel_price * car.fuel_consumption / 100 * distance
        return fuel_cost

    def calculate_product_cost(self, shop: Shop) -> float:
        product_cost = sum(
            self.product_cart[key] * shop.products[key]
            for key in self.product_cart if key in shop.products)
        return product_cost
