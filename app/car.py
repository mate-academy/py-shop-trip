class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_fuel_needed(self, distance_km: float) -> float:
        return distance_km * (self.fuel_consumption / 100)

    def get_fuel_cost(self, distance_km: float, fuel_price: float) -> float:
        fuel_needed = self.get_fuel_needed(distance_km)
        return fuel_price * fuel_needed

    def __repr__(self) -> str:
        return f"{self.brand}({self.fuel_consumption} l/100 km)"
