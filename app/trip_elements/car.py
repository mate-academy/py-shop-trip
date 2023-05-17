from math import sqrt


class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    @staticmethod
    def distance_calculator(start_point: list, end_point: list) -> float:
        first_leg = start_point[0] - end_point[0]
        second_leg = start_point[1] - end_point[1]
        distance = sqrt(first_leg ** 2 + second_leg ** 2)
        return distance

    def gasoline_calculation(self,
                             fuel_cost: float,
                             start_point: list,
                             end_point: list) -> float:
        distance = self.distance_calculator(start_point, end_point)
        amount_of_fuel = distance * self.fuel_consumption / 100
        return amount_of_fuel * fuel_cost
