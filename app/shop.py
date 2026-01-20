from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, int]
