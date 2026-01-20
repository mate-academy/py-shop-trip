from typing import Dict, List


class Shop:
    def __init__(
            self,
            name: str,
            location: List[int],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
