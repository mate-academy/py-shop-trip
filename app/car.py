import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(
        self,
        distance: float,
        fuel_price: float
    ) -> float:
        """Calculate fuel cost for a one-way trip."""
        return distance * self.fuel_consumption / 100 * fuel_price
