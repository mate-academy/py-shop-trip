import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption_for_100_km: float
