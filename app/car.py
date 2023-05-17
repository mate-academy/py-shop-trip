from dataclasses import dataclass


@dataclass
class Car:
    brand: str = "Unknown"
    fuel_consumption: int = 0
