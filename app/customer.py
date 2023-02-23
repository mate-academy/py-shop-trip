from math import dist

from app.shop import Shop

class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def get_distance(self, shop_location: Shop) -> float:
        return dist(self.location, shop_location.location)
