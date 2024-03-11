from math import sqrt


class Car:
    def __init__(
            self,
            initial_location: list[int, int],
            fuel_price: float,
            fuel_consumption: float
    ) -> None:
        self.initial_location = initial_location
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption

    def get_cost_trip(self, destination_location: list[int, int]) -> float:
        x_1, y_1 = self.initial_location
        x_2, y_2 = destination_location
        distance_to_shop = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        distance_to_home = distance_to_shop
        distance = distance_to_shop + distance_to_home
        result = (distance / 100 * self.fuel_consumption * self.fuel_price)
        return round(result, 2)
