from __future__ import annotations


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict
    ):
        self._name = name
        self.product_cart = product_cart
