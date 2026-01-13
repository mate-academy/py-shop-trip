import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_way(self,
                 start_coord: list[int, int],
                 target_coord: list[int, int],
                 fuel_price: int | float) -> int | float:
        delta_x = start_coord[0] - target_coord[0]
        delta_y = start_coord[1] - target_coord[1]
        distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))
        return self.fuel_consumption * distance / 100 * fuel_price
