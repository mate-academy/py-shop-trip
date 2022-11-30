import json
from pathlib import Path


class Customers:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


def create_customer_objects():
    base_dir = Path(__file__).resolve().parent
    # path = os.path.join(os.getcwd(), "config.json")

    with open(base_dir / "config.json", "r") as file:
        data = json.load(file)
        customers = data["customers"]
        customers_list = []
        for customer in customers:
            customers_list.append(Customers(name=customer["name"],
                                            product_cart=customer["product_cart"],
                                            location=customer["location"],
                                            money=customer["money"],
                                            car=customer["car"]))
    return customers_list
