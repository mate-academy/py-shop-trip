import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float
    fuel_price: float

    def calculate_fuel_cost(self, distance: float) -> float:
        fuel_amount = 2 * (self.fuel_consumption / 100) * distance
        return round(fuel_amount * self.fuel_price, 2)
