class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_needed(self, distance_km: float) -> float:
        return (self.fuel_consumption / 100) * distance_km

    def calculate_fuel_cost(
            self,
            distance_km: float,
            fuel_price: float
    ) -> float:
        liters = self.calculate_fuel_needed(distance_km)
        return liters * fuel_price
