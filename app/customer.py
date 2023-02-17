from __future__ import annotations
from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    money: int
    car: Car

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def list_constructor(cls, customers: list) -> list[Customer]:
        customers = [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"],
                    location=customer["location"]
                )
            )
            for customer in customers
        ]
        return customers
