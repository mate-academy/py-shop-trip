class Car:
    def __init__(self, mileage: float) -> None:
        self.mileage_per_km = (mileage / 100)

    def cost_to_drive(self, distance: float, fuel_price: float) -> float:
        return self.mileage_per_km * distance * fuel_price
