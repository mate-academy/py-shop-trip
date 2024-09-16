from dataclasses import dataclass
from app.product import Product


@dataclass
class Shop:
    _name: str
    _location: list
    _products: dict[str: Product]
    _all_shops = []

    @classmethod
    def get_shops(cls) -> list["Shop"]:
        return cls._all_shops

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> list[int, int]:
        return self._location

    @property
    def products(self) -> list[Product]:
        return self._products

    @classmethod
    def create_shops_from_json(cls, json_data: dict) -> None:
        for shop in json_data["shops"]:
            name = shop["name"]
            location = shop["location"]
            products = {name: Product(name, price)
                        for name, price in shop["products"].items()}

            cls._all_shops.append(Shop(name, location, products))
