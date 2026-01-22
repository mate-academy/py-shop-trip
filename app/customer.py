import math
from typing import List, Dict, Any


def calculate_distance(loc1: List[int], loc2: List[int]) -> float:
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: Dict[str, int],
        location: List[int],
        money: float,
        car: Dict[str, Any]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def get_trip_cost(self, shop: Any, fuel_price: float) -> float:
        distance = calculate_distance(self.location, shop.location)
        fuel_needed = (distance * 2 * self.car.fuel_consumption) / 100
        fuel_cost = fuel_needed * fuel_price
        product_cost = sum(
            qty * shop.products[prod]
            for prod, qty in self.product_cart.items()
        )
        return round(fuel_cost + product_cost, 2)
