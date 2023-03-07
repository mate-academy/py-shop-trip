from __future__ import annotations
import dataclasses
import json


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    @staticmethod
    def create_shops(json_file: str) -> list[Shop]:
        with open(json_file, "r") as f:
            data = json.load(f)
            return [Shop(**shop_data) for shop_data in data["shops"]]

    def is_all_products_exist(self, product_cart: dict) -> bool:
        return all(
            product in self.products.keys() for product in product_cart.keys()
        )
