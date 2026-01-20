from typing import List

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
        distance = ((self.location[0] - shop.location[0]) ** 2
                    + (self.location[1] - shop.location[1]) ** 2) ** 0.5 * 2
        trip_cost = round(car.fuel_consumption * distance * fuel_price
                          / 100, 2)
        return trip_cost

    def calculate_product_cost(self, shop: Shop) -> float:
        return sum(
            self.product_cart[key] * shop.products[key]
            for key in self.product_cart if key in shop.products
        )
