from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption_per_100_km: float
    fuel_price: float
