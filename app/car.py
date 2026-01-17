from dataclasses import dataclass


@dataclass
class Car:
    fuel_consumption: int | float
    brand: str
    model: str = None
    year: int = None
    colour: str = None

    def fuel_cost(self,
                  distance: int | float,
                  fuel_price: int | float,
                  ) -> int | float:
        return round(distance * fuel_price * (self.fuel_consumption / 100) * 2,
                     2)
