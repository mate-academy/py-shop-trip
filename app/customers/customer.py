from dataclasses import dataclass


@dataclass
class CustomerCar:
    brand: str
    fuel_consumption: float


@dataclass
class Customer:
    name: str
    product_cart: dict[str: int | float]
    location: list[int, int]
    money: int
    car: CustomerCar


