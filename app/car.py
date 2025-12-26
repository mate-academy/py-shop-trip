from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float | int

    def fuel_price(
            self,
            distance: float | int,
            fuel_price: float | int
    ) -> float | int:
        return distance * self.fuel_consumption / 100 * fuel_price
