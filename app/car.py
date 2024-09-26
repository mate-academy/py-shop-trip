from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def create_customers_car(cls, car: dict[str: str | float]) -> "Car":
        return cls(car["brand"], car["fuel_consumption"])
