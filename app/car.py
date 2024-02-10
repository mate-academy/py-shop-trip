class Car:
    def __init__(self, fuel_consumption: float) -> None:
        self.fuel_consumption = fuel_consumption

    def get_fuel_price(self, distance: float, fuel_price: float) -> float:
        fuel_needed = (distance / 100) * self.fuel_consumption
        cost = fuel_needed * fuel_price
        return cost
