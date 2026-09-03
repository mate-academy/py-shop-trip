class Car:
    def __init__(self, car: dict):
        self.name = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def calculate_fuel_price(self, fuel_price: float | int, distance: float | int) -> float | int:
        return round(distance / 100 * fuel_price * self.fuel_consumption * 2, 2)
