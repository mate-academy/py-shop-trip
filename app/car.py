class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        return fuel_price * ((distance / 100) * self.fuel_consumption)
