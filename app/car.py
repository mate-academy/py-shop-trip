import dataclasses


@dataclasses.dataclass()
class Car:
    brand: str
    fuel_consumption: float

    def trip_cost(self, distance: float, fuel_prise: float) -> float:
        return round(self.fuel_consumption / 100
                     * distance
                     * fuel_prise, 2)
