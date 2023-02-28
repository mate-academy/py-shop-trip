from app.product import Product


class Shop:
    _all_shops = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict[str: Product]
    ) -> None:
        self._name = name
        self._location = location
        self._products = products

    def __str__(self) -> str:
        return f"{self._name}, {self._products}"

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
