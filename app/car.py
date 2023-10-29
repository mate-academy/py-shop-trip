import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: int | float

    def calculate_fuel_cost(
            self,
            first_point: list,
            second_point: list,
            fuel_price: float
    ) -> float:
        distance = ((first_point[0] - second_point[0]) ** 2 + (
                    first_point[1] - second_point[1]) ** 2) ** 0.5

        return (self.fuel_consumption / 100) * distance * fuel_price
