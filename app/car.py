from math import sqrt


class Car:
    def __init__(
            self,
            fuel_price: float,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.fuel_price = fuel_price
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_fuel_to_shop(
            self,
            start_location: list,
            end_location: list
    ) -> float:
        distance = (sqrt((end_location[0] - start_location[0]) ** 2
                         + (end_location[1] - start_location[1]) ** 2))
        fuel_needed = (distance * self.fuel_consumption) / 100
        return fuel_needed * self.fuel_price
