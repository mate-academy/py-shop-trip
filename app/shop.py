from __future__ import annotations
import datetime

from app.location import Location
from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: Location,
        products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return (
            "Shop("
            f"name={self.name}, "
            f"location={self.location}, "
            f"products={self.products}"
            ")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_dict(cls, data: dict) -> Shop:
        return cls(
            name=data.get("name", ""),
            location=Location(*data.get("location", [0, 0])),
            products=data.get("products", {})
        )

    def calculate_cost(
        self,
        product_cart: dict
    ) -> tuple[float, dict]:
        cost = 0.0
        products_to_buy = {}
        for product in product_cart:
            price = self.products[product] * product_cart[product]
            products_to_buy[product] = {
                "count": product_cart[product],
                "price": price
            }
            cost += price
        return (cost, products_to_buy)

    def print_purchase(self, customer: Customer) -> None:
        total, products_to_buy = self.calculate_cost(customer.product_cart)

        print()
        print(f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, purchase in products_to_buy.items():
            formated_price = f'{purchase["price"]:.2f}'.rstrip("0").rstrip(".")
            print(
                f'{purchase["count"]} {product}s '
                f"for {formated_price} dollars"
            )
        print(f"Total cost is {round(total, 2)} dollars")
        print("See you again!")
        print()
