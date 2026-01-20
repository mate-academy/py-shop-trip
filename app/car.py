from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    f_consumption: float

    def price_per_1km(self, fuel_price: float) -> float:
        return self.f_consumption * fuel_price / 100
