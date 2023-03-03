import math


class Car:
    def __init__(self,
                 fuel_price: int,
                 fuel_consumption: int) -> None:
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption

    def trip_to_shop(self,
                     customer_location: list,
                     shop_location: list) -> float:
        total_km = (
            math.sqrt((shop_location[0] - customer_location[0]) ** 2
                      + (shop_location[1] - customer_location[1]) ** 2) * 2
        )
        cost_for_trip = (total_km * self.fuel_consumption
                         / 100 * self.fuel_price)
        return round(cost_for_trip, 2)
