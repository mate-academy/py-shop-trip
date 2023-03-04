import json
import os

from module.customer import Customer


class Shop:
    shops = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def load_from_json_info_about_shop(cls) -> None:
        path_file = os.path.abspath(".")
        path_file = os.path.join(path_file, "config.json")
        with open(path_file, "r") as shop_file:
            shop_data = json.load(shop_file)
            for shop in shop_data["shops"]:
                shop = cls(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"],
                )
                cls.shops.append(shop)

    @staticmethod
    def buy_product(
            customer: Customer,
            name_shop: str,
            products: list
    ) -> None:
        for shop in Shop.shops:
            if shop.name == name_shop:
                name_product = {}
                for product in products:
                    name_product["price"] = customer.product_cart[product] \
                        * shop.products[product]
                    print(f"{customer.product_cart[product]} {product}s for "
                          f"{name_product['price']} dollars")
