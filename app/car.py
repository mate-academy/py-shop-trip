# flake8: noqa
from decimal import Decimal, getcontext

getcontext().prec = 10

class Car:
    fuel_price = Decimal("2.4")

    def __init__(
            self,
            brand: str,
            fuel_consumption: float | int) -> None:
        self.brand = brand
        self.fuel_consumption = Decimal(str(fuel_consumption))

    def ride_to_the_shop(
            self,
            current_location: list[int | float],
            destination: list[int | float]) -> int | float:

        # Convert values to Decimal for precision
        x1, y1 = map(Decimal, map(str, current_location))
        x2, y2 = map(Decimal, map(str, destination))

        # Calculate Euclidean distance
        kms_ridden = (Decimal.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

        # Calculate fuel consumed
        liters_consumed = (self.fuel_consumption * kms_ridden) / 100

        # Calculate fuel cost
        return liters_consumed * Car.fuel_price
