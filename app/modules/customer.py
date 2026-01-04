from typing import TypedDict


class Car(TypedDict):
    brand: str
    fuel_consumption: float


class ProductCart(TypedDict):
    milk: int
    bread: int
    butter: int


class Customer(TypedDict):
    name: str
    product_cart: ProductCart
    location: list[int]
    money: int
    car: Car
