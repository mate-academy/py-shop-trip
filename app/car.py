from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: int | float

    def fuel_cost(
            self,
            distance: int | float,
            fuel_price: int | float
    ) -> float:

        return (distance / 100) * self.fuel_consumption * fuel_price
