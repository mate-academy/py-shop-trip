from __future__ import annotations

from app.car import Car


class Customer:
    def __init__(
        self, name: str, products: dict, location: list, money: int, car: Car
    ) -> None:
        self._name = name
        self._products = products
        self._location = location
        self._money = money
        self._car = car

    @classmethod
    def create_customer(cls, customer_info: dict) -> Customer:
        try:
            return cls(
                customer_info["name"],
                customer_info["product_cart"],
                customer_info["location"],
                customer_info["money"],
                Car.create_car(customer_info["car"]),
            )
        except KeyError as e:
            print(e, "not exist")

    @property
    def name(self) -> str:
        return self._name

    @property
    def products(self) -> dict:
        return self._products

    @property
    def location(self) -> list:
        return self._location

    @property
    def car(self) -> Car:
        return self._car

    @property
    def money(self) -> int | float:
        return self._money

    @money.setter
    def money(self, money: int | float) -> None:
        self._money = money
