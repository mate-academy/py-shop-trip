class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calc_fuel_consumption(self, distance: float) -> float:
        return self.fuel_consumption / 100 * distance
