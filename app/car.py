class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def car_dict(self):
        car = [self.brand, self.fuel_consumption]
        return car
