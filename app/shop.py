from typing import List


class Shop:
    def __init__(
            self,
            name: str,
            location: List[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
