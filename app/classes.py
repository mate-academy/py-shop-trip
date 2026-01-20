from dataclasses import dataclass
from typing import Any


class Creation:
    @classmethod
    def create_class(cls, dict_: dict) -> Any:
        return cls(*dict_.values())


@dataclass
class Customer(Creation):
    name: str
    product_cart: float
    location: list
    money: int | float
    car: dict


@dataclass
class Car(Creation):
    brand: str
    fuel_consumption: float


@dataclass
class Shop(Creation):
    name: str
    location: list
    products: dict
