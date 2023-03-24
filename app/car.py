class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __str__(self) -> str:
        return f"{self.brand} ({self.fuel_consumption} L/100km)"

    def trip_cost(self, distance: float, fuel_price: float) -> float:
        return (self.fuel_consumption / 100) * distance * fuel_price
