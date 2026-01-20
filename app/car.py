from app.config import config


class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float) -> float:
        return self.fuel_consumption * distance / 100 * config["FUEL_PRICE"]
