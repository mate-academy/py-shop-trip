class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self,
                            distance_km: float,
                            fuel_price: float
                            ) -> float:
        liters_used = (distance_km / 100.0) * self.fuel_consumption
        return liters_used * fuel_price
