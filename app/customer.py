from decimal import Decimal
from app.car import Car
from app.config import data_config


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: (int, float),
            car: "Car"
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = Decimal(str(money))
        self.car = car


customers = []
for customer in data_config["customers"]:
    customer = Customer(customer["name"], customer["product_cart"],
                        customer["location"],
                        customer["money"], Car(**customer["car"]))
    customers.append(customer)
