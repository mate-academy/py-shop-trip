from typing import Dict, List, Tuple


class Shop:
    def __init__(
            self,
            name: str,
            location: List[Tuple[int, int]],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
