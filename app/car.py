import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: int | float
