class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float, fuel_price: float):
        return distance * (self.fuel_consumption / 100) * fuel_price

