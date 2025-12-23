class Car:
    def __init__(self, brand: str, fuel_consumption: float | int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def trip_price(self, distance: float | int,
                   fuel_price: float | int) -> float | int:
        return (self.fuel_consumption / 100) * distance * fuel_price
