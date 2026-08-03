from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.location = customer_data["location"]
        self.home_location = customer_data["location"]
        self.money = customer_data["money"]
        self.car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"]
        )

    def calculate_distance(self, target_location: list[int]) -> float:
        return sqrt(
            ((target_location[0] - self.home_location[0]) ** 2)
            + ((target_location[1] - self.home_location[1]) ** 2)
        )

    def evaluate_trip(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = self.calculate_distance(shop.location)
        cost_of_fuel = self.car.calculate_fuel_cost(
            distance_to_shop, fuel_price
        )
        cost_of_cart = shop.calculate_cart_cost(self.product_cart)
        return round((cost_of_fuel * 2) + cost_of_cart, 2)

    def travel_to(self, target_location: list[int]) -> None:
        self.location = target_location

    def pay(self, amount: float) -> None:
        self.money -= amount
