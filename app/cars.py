from math import sqrt


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_comsumption = fuel_consumption

    def fuel_costs(self,
                   location1: list,
                   location2: list,
                   fuel_price: float) -> float:
        distance = sqrt((location2[0] - location1[0]) ** 2
                        + (location2[1] - location1[1]) ** 2)
        return self.fuel_comsumption * fuel_price * 2 * distance / 100
