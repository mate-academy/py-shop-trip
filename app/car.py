from math import sqrt


class Car:
    fuel_price = 0

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def transit_cost(self,
                     shop_location: list[int],
                     customer_location: list[int]
                     ) -> float:
        distance = sqrt(pow(shop_location[0] - customer_location[0], 2)
                        + pow(shop_location[1] - customer_location[1], 2))

        fuel = (distance * 2) * self.fuel_consumption / 100
        return fuel * Car.fuel_price
