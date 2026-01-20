import dataclasses
from typing import List, Dict
from math import dist
from datetime import datetime
from .car import Car
from .shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[float]
    money: float
    car: Car

    def calculate_product_cost(self, shop: Shop) -> float:
        try:
            return sum(
                shop.products[product] * quantity
                for product, quantity in self.product_cart.items()
            )
        except KeyError:
            return None

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) \
            -> float | None:
        if not all(product in shop.products for product in self.product_cart):
            return None

        distance_to_shop = dist(self.location, shop.location)
        round_trip_distance = distance_to_shop * 2
        fuel_needed = self.car.fuel_needed(round_trip_distance)
        fuel_cost = fuel_needed * fuel_price
        product_cost = self.calculate_product_cost(shop)
        return fuel_cost + product_cost

    def buy(self, shop: Shop, fuel_price: float, date: datetime) -> None:
        distance = dist(self.location, shop.location)
        self.location = shop.location[:]

        product_cost = self.calculate_product_cost(shop)
        fuel_cost = self.car.fuel_needed(distance * 2) * fuel_price
        total_cost = product_cost + fuel_cost
        self.money -= total_cost

        # Receipt
        print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            unit_price = shop.products[product]
            print(f"{quantity} {product}s "
                  f"for {unit_price * quantity:g} dollars")
        print(f"Total cost is {product_cost} dollars")
        print("See you again!\n")

        self.location = self.location[:]
