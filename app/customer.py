from app.shop import Shop
from math import dist


class Customer:
    def __init__(self, customers: dict) -> None:
        self.name = customers["name"]
        self.product_cart = customers["product_cart"]
        self.location = customers["location"]
        self.money = customers["money"]
        self.car = customers["car"]

    def money(self) -> None:
        print(f"{self.money}")

    def calculate_distance(self, shop: Shop) -> float:
        return dist(self.location, shop.location)
