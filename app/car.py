import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    def get_brand(self) -> str:
        return self.brand

    def get_fuel_consumption(self) -> float:
        return self.fuel_consumption
