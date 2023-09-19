import math
from typing import Dict, Any, List
from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(self, info: Dict[str, Any], fuel_price: float) -> None:
        self.name = info["name"]
        self.product_cart = info["product_cart"]
        self.location = info["location"]
        self.money = float(info["money"])  # Convert money to float
        self.car = Car(info["car"], fuel_price)
        self.possible_trips = {}

    def calculate_products_cost(self, shop: Shop) -> float:
        products_cost = 0.0
        for product, amount in self.product_cart.items():
            if product in shop.products:
                products_cost += float(amount) * float(shop.products[product])
        return round(products_cost, 2)

    def calculate_distance_to_shop(self, shop_location: List[float]) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return round(distance, 2)

    def calculate_trip_cost(self, shop: Shop) -> float:
        distance = self.calculate_distance_to_shop(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance)
        products_cost = self.calculate_products_cost(shop)
        total = round(products_cost + fuel_cost, 2)
        print(f"{self.name}'s trip to {shop.name} costs {total:.2f}")
        self.possible_trips[total] = shop
        return total

    def go_home(self) -> None:
        print(f"{self.name} rides home")
