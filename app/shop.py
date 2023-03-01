from __future__ import annotations
from app.location import Location


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = Location(location)
        self.products = products

    @classmethod
    def from_dict(cls, info: dict) -> Shop:
        return cls(**info)

    def get_food_cost(self, goods: dict) -> float:
        food_cost = sum(
            quantity * self.products.get(name)
            for name, quantity in goods.items()
        )
        return food_cost
