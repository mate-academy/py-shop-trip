from typing import List


class Shop:

    def __init__(self, shop_dictionary: dict) -> None:
        self.name = shop_dictionary.get("name")
        self.location = shop_dictionary.get("location")
        self.products = shop_dictionary.get("products")

    def __repr__(self) -> str:
        return (
            f"\nShop name: {self.name},"
            f"location: {self.location},"
            f"products available: {self.products}"
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> List[int]:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Name should be a string!")
        self._name = new_name

    @location.setter
    def location(self, new_location: List[int]) -> None:
        if not isinstance(new_location, list):
            raise TypeError("Location should be a list!")
        if not len(new_location) == 2:
            raise ValueError("Location should contain only 2 coordinates!")
        if not all(isinstance(elem, int) for elem in new_location):
            raise ValueError("Coordinates should be integers!")
        self._location = new_location

    @products.setter
    def products(self, new_products: dict) -> None:
        if not isinstance(new_products, dict):
            raise TypeError("Products should be in list")
        if not all(isinstance(key, str) for key in new_products.keys()):
            raise TypeError("Keys in product list should be strings")
        if not all(isinstance(value, float)
                   or isinstance(value, int)
                   for value in new_products.values()):
            raise TypeError("Values in product list should be numeric")
        if any(value < 0 for value in new_products.values()):
            raise ValueError("Values in product list should be positive")
        self._products = new_products
