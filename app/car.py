from math import sqrt


class Car:
    def __init__(
        self, brand: "str", fuel_consumption: float, fuel_price: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def calculate_road_cost(
            self,
            base_location: list[int],
            new_location: list[int]
    ) -> float:
        distance = sqrt(
            (new_location[0] - base_location[0]) ** 2
            + (new_location[1] - base_location[1]) ** 2
        )

        total_distance = distance * 2
        distance_per_fuel = total_distance / 100
        fuel_cost = distance_per_fuel * self.fuel_consumption * self.fuel_price

        return fuel_cost
