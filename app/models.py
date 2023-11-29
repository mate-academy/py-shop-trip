from __future__ import annotations


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float | int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return self.name


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __repr__(self) -> str:
        return self.brand


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return self.name
