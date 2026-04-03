import math


class Car:
    def __init__(self, name: str, fuel_consumption: float) -> None:
        self.name = name
        self.fuel_consumption = fuel_consumption

    def cost_fuel(
            self,
            loc_cus: list,
            loc_shop: list,
            fuel_price: float
    ) -> float:
        distance = math.dist(loc_cus, loc_shop)
        return ((distance * self.fuel_consumption) / 100 * fuel_price) * 2
