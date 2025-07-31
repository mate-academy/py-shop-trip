import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_dict(cls, data: dict) -> list["Shop"]:
        shops = []
        for shop in data:
            shops.append(
                cls(shop["name"], shop["location"], shop["products"])
            )

        return shops

    @staticmethod
    def format_price(price) -> str:
        return str(int(price)) if price == int(price) else f"{price:.1f}"

    def print_receipt(self, customer: "Customer") -> None:
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        _sum = 0
        for product in customer.product_cart:
            total_price_for_product = (customer.product_cart[product]
                                       * self.products[product])
            _sum += total_price_for_product
            print(f"{customer.product_cart[product]} {product}s for "
                  f"{self.format_price(total_price_for_product)} dollars")
        print(f"Total cost is {_sum} dollars")
        print("See you again!\n")
