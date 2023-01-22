from typing import Any

from app.location import Location


class Shop:
    def __init__(self, shop: dict[str, Any]) -> None:
        self.name = shop["name"]
        self.location = Location(shop["location"])
        self.products = shop["products"]

    def check_if_has_products(self, products_to_buy: dict[str, int]) -> bool:
        for product in products_to_buy:
            if product not in self.products:
                return False
        return True

    def get_price_of_products(
            self,
            products_to_buy: dict[str, int]
    ) -> int | float:
        return sum(
            [
                self.products[product] * quantity
                for product, quantity in products_to_buy.items()
            ]
        )
