class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]
