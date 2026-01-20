from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_cost(self,
                  distance: float,
                  fuel_price: float
                  ) -> float:
        return (distance * (self.fuel_consumption / 100)) * fuel_price
