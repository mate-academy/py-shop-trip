from typing import Dict, Tuple


class Shop:
    def __init__(self, name: str, location: Tuple[int, int],
                 products: Dict[str, float]) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = products
