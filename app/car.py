class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_needed_for_trip(self, distance: float | int) -> float:
        return (self.fuel_consumption / 100) * distance
