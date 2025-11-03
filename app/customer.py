from dataclasses import dataclass
from typing import List, Dict
import math
from datetime import datetime
from .car import Car
from .shop import Shop


@dataclass
class Customer:
    name: str
    location: List[float]
    cart: Dict[str, int]
    money: float
    car: Car


    def calculate_distance_to_shop(self, shop: "Shop") -> float:
        """
        Calculate the distance to the shop.
        """
        return math.sqrt((self.location[0] - shop.location[0]) ** 2
                         + (self.location[1] - shop.location[1]) ** 2)


    def calculate_trip_cost(self, shop: "Shop", fuel_price: float) -> float:
        """
        Calculate the total cost of the trip.
        """
        #  dystans do sklepu
        distance = self.calculate_distance_to_shop(shop)
        #  koszty paliwa
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price) * 2
        #  koszty zakupow
        shopping_cost = shop.calculate_cart_cost(self.cart)
        #  suma
        total_cost = shopping_cost + fuel_cost

        return total_cost


