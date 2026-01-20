from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Car:
    fuel_price: ClassVar[float]
    brand: str
    fuel_consumption: int
