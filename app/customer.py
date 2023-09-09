from __future__ import annotations
from math import pow, sqrt

from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def get_info_from_json_file(cls, data_from_json: dict) -> Customer:
        attributes = ["name", "product_cart", "location", "money", "car"]

        return cls(
            *[
                data_from_json[attribute] for attribute in attributes
            ]
        )

    def calculate_distance_to_shop(
            self,
            shop_location: list[int, int]
    ) -> float:
        distance_to_shop = sqrt(
            pow(shop_location[0] - self.location[0], 2)
            + pow(shop_location[1] - self.location[1], 2)
        )

        return distance_to_shop

    def calculate_fuel_cost(
            self,
            distance_in_km: float,
            fuel_price: float
    ) -> float:
        return round(
            distance_in_km * self.car.get("fuel_consumption") / 100
            * fuel_price * 2,
            2
        )

    def calculate_total_cost_in_shop(self, shop_prices: Shop) -> int:
        product_list = ["milk", "bread", "butter"]
        return sum(
            self.product_cart.get(product) * shop_prices.products.get(product)
            for product in product_list
        )

    def print_detailed_purchase_report(self, shop_prices: Shop) -> None:
        print("You have bought: ")
        products = ["milk", "bread", "butter"]
        for product in products:
            product_amount = self.product_cart.get(product)
            print(f"{product_amount} {product}s "
                  f"for {shop_prices.products.get(product) * product_amount}"
                  f" dollars")
        print(f"Total cost is "
              f"{self.calculate_total_cost_in_shop(shop_prices)} dollars")
        print("See you again!\n")
