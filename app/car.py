class Car:
    def __init__(self, brand: str, fuel_consumption: float):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def ride(self):
        pass


class GasStation:
    def __init__(self, fuel_price: float):
        self.fuel_price = fuel_price
