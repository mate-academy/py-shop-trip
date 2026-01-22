from __future__ import annotations

import datetime
from dataclasses import dataclass

from app.customer import Customer
from app.location import Location, create_location_from_list


@dataclass
class Shop:
    name: str
    location: Location
    products: dict

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Shop) -> bool:
        if isinstance(other, Shop):
            return self.name == other.name and self.location == other.location
        return False

    def buy_products_from_cart(self, product_cart: dict) -> int | float:
        cart_price = 0
        for product, quantity in product_cart.items():
            cart_price += self.products[product] * quantity

        return cart_price

    def buy_product(self, product_name: str, quantity: int) -> str:
        price = self.products[product_name] * quantity
        return (f"{quantity} {product_name}s for "
                f"{int(price) if price % 1 == 0 else price} dollars\n")

    def print_check(self, customer: Customer) -> str:
        current_date_time = datetime.datetime.now()
        check_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
        check_bought = [
            self.buy_product(product, quantity)
            for product, quantity
            in customer.product_cart.items()
        ]
        total_price = self.buy_products_from_cart(customer.product_cart)

        return (
            f"Date: {check_time}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:\n"
            f"{''.join(check_bought)}"
            f"Total cost is {total_price} dollars\n"
            "See you again!\n"
        )


def create_shop_from_dict(shop: dict) -> Shop:
    return Shop(
        name=shop["name"],
        location=create_location_from_list(shop["location"]),
        products=shop["products"]
    )
