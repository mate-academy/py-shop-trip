import math


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float,
                 location: list
                 ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.location = location

    def price_trip(self, road_to: list, fuel_price: float) -> float:
        price = (math.sqrt((road_to[0] - self.location[0]) ** 2
                           + ((road_to[1] - self.location[1]) ** 2)) / 100
                 * self.fuel_consumption) * fuel_price
        self.location = road_to.copy()
        return price
