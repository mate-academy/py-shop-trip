class Car:
    def __init__(self, car_info: dict) -> None:
        self.brand: str = car_info["brand"]
        self.fuel_consumption: int | float = car_info["fuel_consumption"]
