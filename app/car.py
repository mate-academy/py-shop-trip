class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_trip(self, km: float, fuel_price: float) -> float:
        return self.fuel_consumption / 100 * km * fuel_price
