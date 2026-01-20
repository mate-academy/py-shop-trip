class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption  # liters per 100 km

    def calculate_trip_cost(self, distance, fuel_price):
        liters_needed = (self.fuel_consumption / 100) * distance
        return liters_needed * fuel_price
