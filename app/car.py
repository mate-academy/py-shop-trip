class Car:
    def __init__(self, data: dict) -> None:
        self.brand = data["brand"]
        self.fuel_consumption = data["fuel_consumption"]
