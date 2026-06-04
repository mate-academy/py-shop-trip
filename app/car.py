class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_fuel_cost(self, distance: float, fuel_cost: float) -> float:
        return (self.fuel_consumption * distance * 2) * fuel_cost / 100
