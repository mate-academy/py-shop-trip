class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_one_km(self) -> float:
        return self.fuel_consumption / 100

    def calculate_fare(self, distance: float, fuel_price: float) -> float:
        return distance * self.cost_one_km() * fuel_price
