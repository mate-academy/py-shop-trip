from app.customer.product_cart import ProductCart
from app.customer.car import Car


class Customer:
    """A class to create a customer."""

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = ProductCart(data["product_cart"])
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"])
