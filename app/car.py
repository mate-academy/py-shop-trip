class Car:
    def __init__(self, data_car: dict) -> None:
        self.brand = data_car["brand"]
        self.fuel_consumption = data_car["fuel_consumption"]
