import json


class Car:
    def __init__(self, configuration: json) -> None:
        self.brand = configuration["car"].get("brand")
        self.fuel_consumption = configuration["car"].get("fuel_consumption")

    def __str__(self) -> str:
        return (f"brand: {self.brand}, "
                f"fuel_consumption: {self.fuel_consumption} ")
