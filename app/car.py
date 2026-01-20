class Car:
    def __init__(self, car):
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def cost_trip(self, distance, fuel_price):
        return self.fuel_consumption * distance * fuel_price / 100
