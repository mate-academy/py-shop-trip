from typing import Any


class Car:
    def __init__(self, characteristics_of_the_car: dict[str, Any]) -> None:
        self._characteristics_of_the_car = characteristics_of_the_car

    def brand_car(self) -> str:
        return self._characteristics_of_the_car["brand"]

    def fuel_consumption(self) -> float:
        return self._characteristics_of_the_car["fuel_consumption"]

    def road_price(self, distance: float, fuel_price: float) -> float:
        amount_of_fuel = (distance / 100) * self.fuel_consumption()
        return (amount_of_fuel * fuel_price) * 2
