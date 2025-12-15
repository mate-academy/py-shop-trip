from dataclasses import dataclass
from typing import List, Dict
from math import dist


@dataclass
class Shop:
    name: str
    location: List[float]
    products: Dict[str, float]

    def calculate_distance(self, customer_location: List[float]) -> float:
        return dist(self.location, customer_location)

    def get_product_price(self, product: str) -> float | int:
        return self.products.get(product)
