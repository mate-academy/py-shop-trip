class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def trip_cost(self, distance, fuel_price):
        return distance * self.fuel_consumption / 100 * fuel_price

    print("LLLL")
