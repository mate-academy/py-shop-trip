from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    brand: str
    fuel_consumption: float  # liters per 100 km

    def fuel_cost_one_way(
            self, distance_km: float, fuel_price: float
    ) -> float:
        liters = distance_km * (self.fuel_consumption / 100)
        return liters * fuel_price

    def fuel_cost_round_trip(
            self, distance_km: float, fuel_price: float
    ) -> float:
        return 2 * self.fuel_cost_one_way(distance_km, fuel_price)
