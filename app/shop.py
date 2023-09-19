import dataclasses

from typing import List, Dict, Union


@dataclasses.dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, Union[int, float]]
