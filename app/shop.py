from typing import List


class Shop:
    def __init__(
        self,
        name: str,
        location: List[int],
        cost_of_products: dict = None
    ) -> None:
        self.name = name
        self.location = location
        self.cost_of_products = {} if None else cost_of_products
