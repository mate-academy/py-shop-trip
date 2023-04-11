from typing import Tuple


class Shop:
    def __init__(
            self,
            name: str,
            location: Tuple[int, int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return self.name
