from __future__ import annotations
from typing import List

from app.classes.class_point import Point


class Shop:
    def __init__(
            self,
            name: str,
            location: Point | List[int, int],
            products: dict
    ) -> None:
        self.name = name
        self.products_prices = products
        self.location = location
        if isinstance(location, list):
            self.location = Point.create_point(location)

    @classmethod
    def create_shop(cls, data_shop: dict) -> Shop:
        return cls(
            name=data_shop["name"],
            location=data_shop["location"],
            products=data_shop["products"]
        )
