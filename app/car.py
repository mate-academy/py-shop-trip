class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self, distance, fuel_price):
        return round(distance / self.fuel_consumption * fuel_price, 2)