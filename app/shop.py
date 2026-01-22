from typing import Tuple, Dict


class Shop:
    def __init__(
            self,
            name: str,
            location: Tuple[int, int],
            products: Dict[str, int]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return self.name
