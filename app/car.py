from dataclasses import dataclass

from app.location import Location


@dataclass
class Car:
    brand: str
    fuel_consumption: float | int

    def get_fuel_cost(
            self,
            start: Location,
            destination: Location,
            fuel_price: float | int
    ) -> float | int:
        distance = start.distance_to(destination)
        consumed_fuel = (self.fuel_consumption * distance) / 100
        return consumed_fuel * fuel_price
