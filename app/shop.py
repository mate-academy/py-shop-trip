from __future__ import annotations


class Shop:
    def __init__(
            self,
            name: str,
            product_price: float,
            location: list[int]
    ) -> None:
        self.name = name
        self.product_price = product_price
        self.location = location
