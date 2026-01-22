from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict

    @classmethod
    def create_shop(cls, shop_data: Dict) -> Shop:
        return Shop(**shop_data)
