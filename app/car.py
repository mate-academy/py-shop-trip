import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self,
                  cust_loc: list[int],
                  shop_loc: list[int],
                  fuel_price: float) -> float:
        fuel = self.fuel_consumption / 100
        return fuel * fuel_price * math.dist(cust_loc, shop_loc)
