from math import sqrt


class Car:
    def __init__(
            self,
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def cost_distance(
            self,
            shop_location: list,
            customer_location: list
    ) -> float:
        x1, y1 = customer_location
        x2, y2 = shop_location
        distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) * 2
        price_one_fuel = self.fuel_consumption / 100 * self.fuel_price
        return round(distance * price_one_fuel, 2)
