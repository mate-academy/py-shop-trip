class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: int
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_km(self) -> float:
        return self.fuel_consumption / 100

    def calculate_fare(
            self,
            distance: int,
            fuel_price: int
    ) -> float:
        return distance * fuel_price * self.cost_km()
