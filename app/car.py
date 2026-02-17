class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_fuel_needed(self, distance: float) -> float:
        return (distance / 100) * self.fuel_consumption
