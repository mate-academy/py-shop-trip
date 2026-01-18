class Car:

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def coast_trip(self, distance: float, fuel_prise: float) -> float:
        return (self.fuel_consumption * distance) / 100 * fuel_prise
