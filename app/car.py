class Car:
    cars = {}

    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        Car.cars[self.brand] = self
