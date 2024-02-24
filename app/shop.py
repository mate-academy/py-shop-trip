from __future__ import annotations


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_price_of_product_cart(self, product_cart: dict) -> float:
        return sum(
            self.products[key] * value
            for key, value in product_cart.items()
        )

    @staticmethod
    def json_list_to_shop_objects(
            shops: list[dict]
    ) -> list[Shop]:
        return [
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            for shop in shops
        ]
