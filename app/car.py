from math import dist


class Car:
    def __init__(self, location: list, fuel_consumption: float) -> None:
        self.x = location[0]
        self.y = location[1]
        self.fuel_consumption = fuel_consumption

    def calculate_price_of_way(self,
                               shop_x: int,
                               shop_y: int,
                               fuel_price: float
                               ) -> float:
        distance = dist([self.x, self.y], [shop_x, shop_y])
        return ((self.fuel_consumption / 100) * distance * fuel_price) * 2
