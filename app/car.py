from dataclasses import dataclass


@dataclass
class Car:
    """Represents a car with its brand and fuel consumption."""
    brand: str
    fuel_consumption: float
