class Car:
    def __init__(self, car: dict):
        self.fuel_consumption = car["fuel_consumption"]

    def road_cost(self, distance: float, fuel_price: float) -> float:
        return fuel_price * (self.fuel_consumption / 100 * distance)
