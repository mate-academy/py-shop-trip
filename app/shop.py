from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, Decimal]

    @staticmethod
    def shops_list(shops: list[dict]) -> list:
        list_of_shops = []
        for shop in shops:
            shop = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            list_of_shops.append(shop)
        return list_of_shops
