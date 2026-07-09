from typing import Any


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_config(cls, data: dict[str, Any]) -> "Shop":
        return cls(
            name=data["name"],
            location=data["location"],
            products=data["products"]
        )
