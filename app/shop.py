from typing import List
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict
