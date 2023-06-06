from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict[str: int]
    location: list[int]
    money: int
    car: Car

    @classmethod
    def create_customers(cls, customers: dict) -> list:
        return [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car.create_customers_car(customer["car"])
            )
            for customer in customers
        ]
