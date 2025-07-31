class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_price_of_trip(self, distance: float,
                                fuel_price: float) -> float:
        return round(distance * self.fuel_consumption / 100 * fuel_price, 2)
