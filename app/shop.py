from typing import Dict, Any


class Shop:
    def __init__(
            self, name: str,
            location: tuple,
            products: Dict[str, Any]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
