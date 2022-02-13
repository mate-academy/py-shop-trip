from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    product_price: dict
    location: list
    money: int
    car: dict


@dataclass
class Shop:
    name: str
    location: list
    products: dict
