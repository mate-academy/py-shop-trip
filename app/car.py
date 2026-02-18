from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def round_trip_fuel_cost(
        self,
        distance_km: float,
        fuel_price: float
    ) -> float:
        liters = (self.fuel_consumption / 100) * distance_km * 2
        return round(liters * fuel_price, 2)
