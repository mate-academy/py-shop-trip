

class Car:
    def __init__(self, brand: str, fuel_consumption: int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_fuel_cost(self, distance: list, fuel_price: int) -> float:
        return (distance / 100) * self.fuel_consumption * fuel_price * 2
