class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_for_trip(self, distance: float, fuel_price: float) -> float:
        return round(distance * self.fuel_consumption * fuel_price / 100, 3)
