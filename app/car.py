class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        distance_fuel = (distance * self.fuel_consumption) / 100
        total_price = distance_fuel * fuel_price
        return total_price
