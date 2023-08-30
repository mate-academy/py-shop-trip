from __future__ import annotations


class ProductCart:
    def __init__(self, product_list: dict = None) -> None:
        if not product_list:
            product_list = {}
        self.product_list = product_list

        for product, number in product_list.items():
            self.product_list[product] = number

    def add_to_cart(self, product: str) -> None:
        self.product_list[product] = self.product_list.get(product, 0) + 1

    def remove_from_cart(self, product: str) -> None:
        self.product_list[product] = self.product_list.get(product, 1) - 1

    @classmethod
    def from_fict(cls, product_cart: dict) -> ProductCart:
        return ProductCart(product_list=product_cart)
