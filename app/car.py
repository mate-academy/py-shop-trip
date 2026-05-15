from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Car:
    brand: str
    fuel_consumption: Decimal
