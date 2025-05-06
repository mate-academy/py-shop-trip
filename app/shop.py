from dataclasses import dataclass
from app.product import Product


@dataclass
class Shop:
    name: str
    location: list
    products: Product

    @classmethod
    def from_dict(cls, params: dict) -> "Shop":
        return cls(
            name=params["name"],
            location=params["location"],
            products=Product(**params["products"])
        )
