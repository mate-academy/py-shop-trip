from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    vol_of_fuel: float | int
