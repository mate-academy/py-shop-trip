from __future__ import annotations

from app.car import Car
from app.location import Location


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: Location,
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return (
            "Customer("
            f"name={self.name}, "
            f"product_cart={self.product_cart}, "
            f"location={self.location}, "
            f"money={self.money}, "
            f"car={self.car}"
            ")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        return cls(
            name=data.get("name", ""),
            product_cart=data.get("product_cart", {}),
            location=Location(*data.get("location", [0, 0])),
            money=data.get("money", 0.0),
            car=Car(**data.get("car"))
        )
