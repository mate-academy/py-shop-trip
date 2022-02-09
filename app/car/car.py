from typing import Union


class Car:
    def __init__(self, brand: str, fuel_consumption: Union[int, float]):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        self._brand = brand

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption: Union[int, float]):
        self._fuel_consumption =\
            fuel_consumption if fuel_consumption >= 0 else 0
