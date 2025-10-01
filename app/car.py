from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float  # литров на 100 км

    def fuel_cost(self, distance_km: float, fuel_price: float) -> float:
        """Посчитать стоимость топлива на заданное расстояние."""
        liters = distance_km * self.fuel_consumption / 100
        return liters * fuel_price
