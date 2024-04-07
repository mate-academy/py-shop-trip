from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import List

import app.auxilaries.parsing_shopping as parsing
from app.auxilaries.car import Car
from app.auxilaries.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int | float
    car: Car

    def get_fuel_cost(self, car: Car, shop: Shop) -> float:
        fuel_price = parsing.parse_data_from_json()[0]
        distance = sqrt((shop.location[0] - self.location[0]) ** 2
                        + (shop.location[1] - self.location[1]) ** 2)
        fuel_cost = fuel_price * car.fuel_consumption / 100 * distance
        return fuel_cost

    def calculate_product_cost(self, shop: Shop) -> float:
        product_cost = 0
        for key in self.product_cart:
            if key in shop.products:
                product_cost += self.product_cart[key] * shop.products[key]

        return product_cost

    def get_home(self, shop: Shop) -> None:
        self.money = self.money - shop.total_cost
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def visit_shop(self, chosen_shop: Shop) -> str:
        shopping_list = []
        receipt_total = 0
        self.location = chosen_shop.location

        for product, quantity in self.product_cart.items():
            product_cost = quantity * chosen_shop.products[product]
            receipt_total += product_cost
            product_cost = parsing.format_money(product_cost)
            shopping_list.append(f"{quantity} {product}s "
                                 f"for {product_cost} dollars")

        receipt_total = parsing.format_money(receipt_total)

        parsing.print_receipt(self.name, shopping_list, receipt_total)
        return receipt_total
