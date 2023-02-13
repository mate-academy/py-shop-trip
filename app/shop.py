from __future__ import annotations


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def create_shop(shop: dict) -> Shop:
        return Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
