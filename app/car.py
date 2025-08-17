class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption  # liters per 100 km

    def fuel_cost(self, distance_km: float, fuel_price: float) -> float:
        liters = (distance_km * self.fuel_consumption) / 100
        return round(liters * fuel_price, 2)
