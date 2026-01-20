from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: int

    def __post_init__(self) -> None:
        self.price_km = self.fuel_consumption / 100
