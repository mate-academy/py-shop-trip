from dataclasses import dataclass
import json
from app.customer import Customers


@dataclass
class Shop:

    name: str
    location: list
    products: dict
    list_of_shops = []

    @classmethod
    def create_shops(cls) -> None:
        with open("app/config.json") as f:
            file_ = json.load(f)
        for shop in file_["shops"]:
            cls.list_of_shops.append(Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            ))


def calculation_of_the_cost_of_purchases(
        customer: Customers,
        shop: Shop
) -> float:
    total_price = 0
    for product, amount in customer.product_cart.items():
        total_price += amount * shop.products[product]
    return total_price
