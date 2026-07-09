from typing import Any


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def from_config(cls, data: dict[str, Any]) -> "Car":
        return cls(
            brand=data["brand"],
            fuel_consumption=data["fuel_consumption"],
        )
