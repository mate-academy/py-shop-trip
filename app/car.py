from math import sqrt


class Car:
    def __init__(self, name: str, fuel_consumption: float) -> None:
        self.name = name
        self.fuel_consumption = fuel_consumption

    def calculate_round_trip_fuel_cost(self, cord_customer: list,
                                       cord_shop: list,
                                       price_fuel: float) -> float:
        distance_price = (sqrt(((cord_customer[0] - cord_shop[0]) ** 2)
                               + ((cord_customer[1] - cord_shop[1]) ** 2))
                          * (self.fuel_consumption / 100) * price_fuel)
        return round(distance_price * 2, 2)
