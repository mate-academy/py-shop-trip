import json
from typing import Any
from pathlib import Path


CONFIG_PATH = Path(__file__).parent / "config.json"

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)
    customers = config["customers"]


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __getitem__(self, item: str) -> Any:
        if item in self.product_cart:
            return self.product_cart[item]
        if hasattr(self, item):
            return getattr(self, item)
        raise KeyError(item)
