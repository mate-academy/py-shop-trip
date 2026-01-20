from __future__ import annotations
import datetime

from app.location import Location
from app.product import Product


class Shop:
    def __init__(
            self,
            name: str,
            location: Location,
            products: list[Product]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def serve_customer(
            self,
            name: str,
            product_cart: list[Product]
    ) -> None:
        self.print_date()
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")

        prod_price = {product.name: product.price for product in self.products}
        for prod in product_cart:
            prod_cost = prod.calculate_cost(prod_price.get(prod.name))
            print(
                f"{prod.quantity} {prod.name}s "
                f"for {prod_cost.normalize()} dollars"
            )

        total_cost = Product.calculate_total_cost(
            product_cart, self.products
        )
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    @staticmethod
    def print_date() -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))

    @classmethod
    def get_shop_from_dict(cls, shop_dict: dict) -> Shop:
        return cls(
            shop_dict["name"],
            Location.get_location(*shop_dict["location"]),
            Product.get_products(shop_products=shop_dict["products"]),
        )

    def __str__(self) -> str:
        return (
            f"Shop name: {self.name}\n"
            f"Shop location: {self.location}\n"
            f"Shop products: {self.products}\n"
        )
