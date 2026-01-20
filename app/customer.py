from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list
    money: int
    car: Car
