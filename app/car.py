class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def price_for_km(self, fuel_price: float) -> float:
        return self.fuel_consumption * fuel_price / 100
