class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        liters_needed = (self.fuel_consumption / 100) * distance
        return liters_needed * fuel_price
