import math
from app.shop import Shop


class Customer:
    def __init__(self, customer_data: dict, fuel_price: float) -> None:
        self.fuel_price = fuel_price
        self.name = customer_data["name"]
        self.location = customer_data["location"]
        self.product_cart = customer_data["product_cart"]
        self.fuel_consumption = customer_data["car"]["fuel_consumption"]
        self.money = customer_data["money"]

    def calculate_distance(self, shop_location: list) -> float:
        return math.dist(self.location, shop_location)

    def calculate_trip_cost(self, shop: Shop) -> float:
        calculated_distance = self.calculate_distance(shop.location)
        fuel_cost \
            = ((calculated_distance * 2)
               * (self.fuel_consumption / 100) * self.fuel_price)
        total_cost = 0
        for product in self.product_cart:
            product_price = shop.products[product]
            total_cost += product_price * self.product_cart[product]
        return fuel_cost + total_cost
