from __future__ import annotations


class Shop:
    def __init__(
            self,
            name: str,
            products: float,
            location: list[int]
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
