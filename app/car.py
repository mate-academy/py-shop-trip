class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def price(self, distance: float, fuel_price: float) -> float:
        fuel_per_km = self.fuel_consumption / 100
        fuel_needed = fuel_per_km * distance
        return fuel_needed * fuel_price
