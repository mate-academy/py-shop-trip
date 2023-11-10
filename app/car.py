from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_expenses(
            self,
            distance: float,
            fuel_price: float
    ) -> float:
        """Returns price for ride in one end"""
        return self.fuel_consumption * distance / 100 * fuel_price
