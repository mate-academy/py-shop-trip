from math import sqrt


class Car:
    fuel_price = 0

    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_comsumption = fuel_consumption

    def fuel_costs(self, location1: list, location2: list) -> float:
        distance = sqrt((location2[0] - location1[0]) ** 2
                        + (location2[1] - location1[1]) ** 2)
        return self.fuel_comsumption * self.fuel_price * 2 * distance / 100
