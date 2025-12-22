class Car:

    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_needed(self, distance, fuel_price):
        fuel_needed = (distance / 100) * self.fuel_consumption
        total_cost = fuel_needed * fuel_price
        return fuel_needed, total_cost