import dataclasses
from typing import List, Dict


@dataclasses.dataclass
class Shop:
    name: str
    location: List[float]
    products: Dict[str, float]
