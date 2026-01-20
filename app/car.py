import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float  # per 100 km

    def fuel_needed(self, distance: float) -> float:
        return (distance / 100.0) * self.fuel_consumption
