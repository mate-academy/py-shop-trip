from __future__ import annotations

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self._name = name
        self._location = location
        self._products = products

    @classmethod
    def create_shop(cls, shop_info: dict) -> Shop:
        try:
            return cls(
                shop_info["name"],
                shop_info["location"],
                shop_info["products"]
            )
        except KeyError as e:
            print(e, "not exist")

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> list:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    def calculate_total_product_cost(self, customer: Customer) -> int:
        products_total_cost = 0
        for product in self._products:
            products_total_cost += (self._products[product]
                                    * customer.products[product])

        return products_total_cost
