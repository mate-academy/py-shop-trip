import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self, distance: float, fuel_price: float) -> float:
        return (distance / 100) * fuel_price * self.fuel_consumption

    @staticmethod
    def calculate_distance(home: list, shop: list) -> float:
        return math.sqrt((shop[0] - home[0]) ** 2 + (shop[1] - home[1]) ** 2)
