from math import sqrt


class Car:
    def __init__(
            self,
            first_point: list,
            second_point: list,
            fuel_price: float,
            fuel_consumption: float
    ) -> None:
        self.first_point = first_point
        self.second_point = second_point
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption

    def get_cost_trip(self) -> float:
        x_1, y_1 = self.first_point
        x_2, y_2 = self.second_point
        distance = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        result = (distance / 100 * self.fuel_consumption * self.fuel_price) * 2
        return round(result, 2)
