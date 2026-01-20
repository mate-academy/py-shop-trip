from __future__ import annotations
import json
from dataclasses import dataclass
from typing import List

from app.customer import Customer
from app.shop import Shop


@dataclass
class Shopping:
    FUEL_PRICE: float
    customers: List[Customer]
    shops: List[Shop]

    @classmethod
    def from_json_file(cls, filename: str) -> Shopping:
        with open(filename, "r") as f:
            data = json.loads(f.read())
            return cls(**data)
