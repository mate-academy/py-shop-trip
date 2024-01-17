import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(self, start_location: list[int],
                            end_location: list[int],
                            fuel_price: float) -> float:
        distance = ((start_location[0] - end_location[0]) ** 2
                    + (start_location[1] - end_location[1]) ** 2) ** 0.5
        return (self.fuel_consumption / 100) * distance * fuel_price
