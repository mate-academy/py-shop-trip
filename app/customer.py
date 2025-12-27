import json
from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: tuple[int, int]
    money: int
    car: Car

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        return cls(
            name=data["name"],
            product_cart=data["product_cart"],
            location=data["location"],
            money=data["money"],
            car=Car(**data["car"])
        )

    @staticmethod
    def load_shops() -> list:
        with open("config.json", "r") as file:
            data = json.load(file)

        return [Customer.from_dict(customer) for customer in data["customers"]]
