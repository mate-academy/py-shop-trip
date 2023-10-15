from dataclasses import dataclass
from typing import List


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict
    total_cost: float = 0
