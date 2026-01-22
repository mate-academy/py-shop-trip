from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Car:
    brand: str
    fuel_consumption: float
