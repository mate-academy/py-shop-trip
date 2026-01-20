class Car:
    def __init__(self, car_data: dict) -> None:
        self.brand = car_data["brand"]
        self.fuel_consumption = car_data["fuel_consumption"]
