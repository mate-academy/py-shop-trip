import math


class Car:
    def __init__(self, brand: str, fuel: float) -> None:
        self.brand = brand
        self.fuel = fuel

    def calculate_road_cost(self, customer_loc: list,
                            shop_loc: list, fuel_price: float) -> float:
        distance = (math.sqrt((customer_loc[0] - shop_loc[0]) ** 2
                              + (customer_loc[1] - shop_loc[1]) ** 2))
        cost = round((distance / 100 * fuel_price * self.fuel) * 2, 2)
        return cost
