class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_fuel_cost(self, distance, fuel_price):
        return distance * self.fuel_consumption * fuel_price / 100.0