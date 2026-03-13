from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(
            self,
            distance: int | float,
            fuel_price: int | float
    ) -> int | float:
        fuel_needed = self.fuel_consumption / 100 * distance
        fuel_cost = fuel_needed * fuel_price
        return fuel_cost


def create_car(car_data: dict) -> Car:
    return Car(
        brand=car_data["brand"],
        fuel_consumption=car_data["fuel_consumption"],
    )
