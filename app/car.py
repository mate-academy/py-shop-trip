class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_trip_cost(
            self, distance_km: float,
            fuel_price: float
    ) -> float:
        liters = (distance_km / 100) * self.fuel_consumption
        cost = liters * fuel_price
        return cost
