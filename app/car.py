from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


class Car:
    FUEL_PRICE = Decimal("0")

    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = Decimal(str(fuel_consumption))

    @classmethod
    def change_fuel_price(cls, price: Decimal) -> None:
        cls.FUEL_PRICE = Decimal(str(price))


class Location:
    """
    I would make a separate class for Location
    and define a method to calculate distance inside of it
    """

    def __init__(self, coordinates: list) -> None:
        self.cord = Decimal(coordinates[0]), Decimal(coordinates[1])

    def calculate_cost_distance(
            self,
            second_coordinate: Location,
            car: Car
    ) -> Decimal:
        distance = (
            (self.cord[0] - second_coordinate.cord[0]) ** 2
            + (self.cord[1] - second_coordinate.cord[1]) ** 2
        ).sqrt()
        cost = distance * 2 * car.fuel_consumption / 100 * car.FUEL_PRICE
        return cost.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
