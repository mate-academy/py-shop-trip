from __future__ import annotations
from app.car import Car
from app.location import Location


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: Location,
                 money: int | float,
                 car: Car
                 ) -> None:
        self._name = name
        self._product_cart = product_cart
        self._current_location = location
        self._money = money
        self._car = car

        self._home_location = Location(location.x, location.y)

    @property
    def name(self) -> str:
        return self._name

    @property
    def product_cart(self) -> dict:
        return self._product_cart

    @property
    def location(self) -> Location:
        return self._current_location

    @location.setter
    def location(self, other: Location) -> None:
        self._current_location = other

    @property
    def money(self) -> int | float:
        return self._money

    @money.setter
    def money(self, other: int | float) -> None:
        self._money = other

    @property
    def car(self) -> Car:
        return self._car

    @property
    def home_location(self) -> Location:
        return self._home_location

    @staticmethod
    def from_dict(customer_dict: dict) -> Customer:
        return Customer(
            name=customer_dict.get("name"),
            product_cart=customer_dict.get("product_cart"),
            location=Location.from_list(customer_dict.get("location")),
            money=customer_dict.get("money"),
            car=Car.from_dict(customer_dict.get("car"))
        )

    def __repr__(self) -> str:
        return (f"Customer(name='{self._name}', "
                f"product_cart={self._product_cart}, "
                f"location={self._current_location}, "
                f"money={self._money}, "
                f"car={self._car})")
