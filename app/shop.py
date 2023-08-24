import dataclasses
from typing import Dict
from decimal import Decimal


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: Dict[str, Decimal]
