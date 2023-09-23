import math


class Car:

    def __init__(self, brand: int, fuel_consumption: float) -> None:

        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_of_fuel(self,
                     customer_location: list,
                     shop_location: list,
                     fuel_cost: float) -> float:
        distance = round((math.dist(customer_location, shop_location) * 2), 2)
        return round((self.fuel_consumption / 100 * distance * fuel_cost), 2)
