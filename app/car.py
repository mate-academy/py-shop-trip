class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self, distance: float, fuel_price: float) -> float:
        liters = distance * self.fuel_consumption / 100
        return liters * fuel_price
