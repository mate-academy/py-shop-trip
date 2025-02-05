from .car import Car
from .shop import Shop
import math
from typing import Dict, List, Any


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: Dict[str, int],
                 location: List[float],
                 money: float,
                 car: Dict[str, Any]) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_distance(self, shop_location: List[float]) -> float:
        return math.sqrt(
            (shop_location[0] - self.location[0]) ** 2
            + (shop_location[1] - self.location[1]) ** 2
        )

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price)
        product_cost = shop.calculate_product_cost(self.product_cart)
        total_cost = fuel_cost * 2 + product_cost  # Round trip
        return round(total_cost, 2)

    def make_purchase(self, shop: Shop, fuel_price: float) -> None:
        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        if self.money >= trip_cost:
            self.money -= trip_cost
            self.location = shop.location
            total_cost = shop.calculate_product_cost(self.product_cart)
            shop.print_receipt(self.name, self.product_cart, total_cost)
            self.location = [12, -2]
            print(f"{self.name} rides home")
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop\n")
