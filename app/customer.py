import json
from typing import List, Dict
from math import sqrt
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: List[float],
            money: float, car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_shopping_cost(self, shop: None) -> float:
        with open("app/config.json") as f:
            config = json.load(f)

        distance_to_shop = sqrt(
            (self.location[0] - shop.location[0])
            ** 2 + (self.location[1] - shop.location[1])
            ** 2
        )

        fuel_cost_to_shop = (distance_to_shop * self.car.fuel_consumption
                             / 100
                             ) * config["FUEL_PRICE"]
        total_products_cost = self.calculate_products_cost(shop)
        fuel_cost_to_home = fuel_cost_to_shop
        total_cost = (fuel_cost_to_shop
                      + total_products_cost
                      + fuel_cost_to_home
                      )
        return total_cost

    def calculate_products_cost(self, shop: None) -> float:
        total_cost = 0
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                total_cost += shop.products[product] * quantity
        return total_cost
