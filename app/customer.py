import json


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money


with open("app/config.json") as config:
    data = json.load(config)
    customer_list = [Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"])
        for customer in data["customers"]]
