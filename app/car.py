class Car:
    def __init__(
        self,
        brand: str,
        fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_to_shop(self, distance: float) -> float:
        return (distance * self.fuel_consumption) / 100
