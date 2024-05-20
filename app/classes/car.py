from __future__ import annotations
from app.classes.from_dict import FromDict


class Car(FromDict):
    def __init__(self,
                 brand: str = "",
                 fuel_consumption: int | float = 0.0) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def from_dict(cls_dict: dict) -> Car:
        new_car = Car()
        for key in cls_dict:
            setattr(new_car, key, cls_dict[key])
        return new_car
