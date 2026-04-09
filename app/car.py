class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_fuel_needed(self, distance: int | float) -> int | float:
        fuel_needed = (distance * self.fuel_consumption) / 100
        return fuel_needed
