import math
from datetime import datetime
from typing import List, Dict
from .car import Car
from .shop import Shop


class Customer:
    def __init__(
        self, name: str, product_cart: Dict[str, int],
        location: List[int], money: float, car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_cost_to_shop = self.car.calculate_fuel_cost(distance, fuel_price)
        product_cost = self.calculate_product_cost(shop)
        fuel_cost_to_home = self.car.calculate_fuel_cost(distance, fuel_price)
        return fuel_cost_to_shop + product_cost + fuel_cost_to_home

    def calculate_distance(self, shop_location: List[int]) -> float:
        return math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )

    def calculate_product_cost(self, shop: Shop) -> float:
        return sum(
            self.product_cart[product] * shop.products[product]
            for product in self.product_cart
            if product in shop.products
        )

    def buy_products(self, shop: Shop) -> None:
        now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in self.product_cart.items():
            cost = shop.products[product] * quantity
            print(f"{quantity} {product}s for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        self.money -= total_cost

    def update_location(self, new_location: List[int]) -> None:
        self.location = new_location
