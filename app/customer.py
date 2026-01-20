from app.car import Car
from app.point import Point


class Customer:
    def __init__(self, cust_data: dict) -> None:
        self.name = cust_data["name"]
        self.product_cart = cust_data["product_cart"]
        self.location = Point(cust_data["location"])
        self.money = cust_data["money"]
        self.car = Car(cust_data["car"])
