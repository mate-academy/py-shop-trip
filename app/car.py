class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_trip(self, distance: float, fuel_price: int) -> float:

        return (self.fuel_consumption / 100) * distance * fuel_price
