from __future__ import annotations

from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int | float
    car: Car

    @classmethod
    def get_customer_info(cls, customer: dict) -> Customer:
        return cls(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
