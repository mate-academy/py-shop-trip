from typing import List, Dict


class Shop:
    def __init__(
            self,
            location: List[int],
            products: Dict[str, int]
    ) -> None:
        self.location = location
        self.products = products
