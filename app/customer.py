from app.car import Car
from app.location import Location


class Customer:
    def __init__(self, customer: dict):
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = Location(customer["location"])
        self.money = customer["money"]
        self.car = Car(customer["car"])
