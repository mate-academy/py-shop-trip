from __future__ import annotations
from app.location import Location


class Shop:
    def __init__(self, name: str, location: Location, products: dict) -> None:
        self._name = name
        self._location = location
        self._products = products

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> Location:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    @staticmethod
    def from_dict(shop_dict: dict) -> Shop:
        return Shop(
            name=shop_dict.get("name"),
            location=Location.from_list(shop_dict.get("location")),
            products=shop_dict.get("products")
        )

    def __repr__(self) -> str:
        return (f"Shop(name='{self._name}', "
                f"location={self._location}, "
                f"products={self._products})")
