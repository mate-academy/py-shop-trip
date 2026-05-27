from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customers import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def buy_products(self, customer: "Customer") -> dict:
        cart = {}
        for product, price in self.products.items():
            count_products = customer.product_cart[product]
            for_one_pos = count_products * price
            if for_one_pos == int(for_one_pos):
                for_one_pos = int(for_one_pos)
            cart[product] = (count_products, for_one_pos)
        return cart
