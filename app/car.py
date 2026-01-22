from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float


def create_car_from_dict(car: dict) -> Car:
    return Car(
        brand=car["brand"],
        fuel_consumption=car["fuel_consumption"]
    )
