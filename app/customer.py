from dataclasses import dataclass, field
from typing import List, Dict

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str = ""
    products_cart: Dict[str, int] = field(default_factory=dict)
    location: List[int] = field(default_factory=list)
    money: int = 0
    car: Car = None
    trips_costs: Dict[str, float] = field(default_factory=dict)
    chosen_shop: Shop = None
