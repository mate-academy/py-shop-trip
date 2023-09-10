class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.fuel_consumption = fuel_consumption / 100
        self.brand = brand


def create_car(car: dict) -> Car:
    return Car(brand=car["brand"],
               fuel_consumption=car["fuel_consumption"])
