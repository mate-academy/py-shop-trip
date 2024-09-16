class Car:
    def __init__(self, car: dict):
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def calc_fuel_consumption(self, distance: float) -> float:
        return self.fuel_consumption / 100 * distance
