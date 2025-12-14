class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_ride(
            self,
            actual_location: list,
            destination: list,
            fuel_price: float = 2.4
    ) -> float:
        x1, y1 = actual_location
        x2, y2 = destination
        distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        cost = distance * (self.fuel_consumption / 100) * fuel_price
        return cost * 2
