class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_cost_trip(self, distance: float, fuel_price: float) -> float:
        trip_price = (self.fuel_consumption / 100) * distance * fuel_price

        return trip_price
