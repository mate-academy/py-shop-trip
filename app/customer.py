from dataclasses import dataclass
from typing import List, Dict

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[int]
    money: float
    car: Car

    def __post_init__(self) -> None:
        self.home = self.location.copy()

    def change_location(self, new_location: List[int]) -> None:
        self.location = new_location
