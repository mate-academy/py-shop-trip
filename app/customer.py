import math
from typing import Dict

from app import Shop
from app.car import Car


class Customer:
    def __init__(self, name: str, product_cart: Dict[str, int],
                 location: tuple, money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def add_to_cart(self, product: str, quantity: int) -> None:
        self.product_cart[product]\
            = self.product_cart.get(product, 0) + quantity

    def calculate_distance(self, store_location: tuple) -> float:
        if hasattr(store_location, "location"):
            store_location = store_location.location
        return math.sqrt(
            (store_location[0] - self.location[0]) ** 2
            + (store_location[1] - self.location[1]) ** 2
        )

    def calculate_trip_cost(self, store_location: tuple,
                            fuel_price: float) -> float:
        distance = self.calculate_distance(store_location)
        fuel_needed = (distance / 100) * self.car.fuel_consumption
        trip_cost = fuel_needed * fuel_price
        return round(trip_cost, 2)

    def choose_cheapest_store(self, shops: Dict[str, Shop],
                              fuel_price: float) -> str:
        cheapest_store = None
        lowest_price = float("inf")
        for shop_name, shop in shops.items():
            trip_cost = self.calculate_trip_cost(shop.location, fuel_price)
            purchase_cost = shop.calculate_purchase_cost(self.product_cart)
            total_cost = trip_cost + purchase_cost
            if total_cost < lowest_price:
                lowest_price = total_cost
                cheapest_store = shop_name
        return cheapest_store

    def purchase(self, total_cost: float) -> bool:
        if self.money >= total_cost:
            self.money -= total_cost
            return True
        return False

    def return_home(self, store_location: tuple, fuel_price: float) -> float:
        return self.calculate_trip_cost(store_location, fuel_price)
