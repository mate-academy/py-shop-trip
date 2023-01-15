class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def fuel_needed_for_trip(self, distance: int | float) -> int | float:
        return self.fuel_consumption * distance / 100
