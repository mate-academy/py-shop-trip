from __future__ import annotations

from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict[str, float]
    location: list[int]
    money: int
    car: Car

    @classmethod
    def from_dict(cls, customer: dict) -> Customer:
        return cls(name=customer["name"],
                   product_cart=customer["product_cart"],
                   location=customer["location"],
                   money=customer["money"],
                   car=Car.from_dict(customer["car"]))
