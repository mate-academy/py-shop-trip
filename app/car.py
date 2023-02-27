from math import sqrt


class Car:

    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.__fuel_price = 0

    @property
    def fuel_price(self) -> int | float:
        return self.__fuel_price

    @fuel_price.setter
    def fuel_price(self, value: int | float) -> None:
        self.__fuel_price = value

    def calculates_fuel_cost_per_km(self) -> float:
        return (self.fuel_consumption * self.__fuel_price) / 100

    @staticmethod
    def calculates_trip_cost_to_shop(
            customer: object,
            shop: object
    ) -> int | float:
        trip_cost_to_shop = (
            sqrt(
                (shop.location[0] - customer.location[0]) ** 2
                + (shop.location[1] - customer.location[1]) ** 2
            )
            * customer.car.calculates_fuel_cost_per_km()
        )
        return trip_cost_to_shop * 2
