import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class Car:
    brand: str
    consumption: Decimal
