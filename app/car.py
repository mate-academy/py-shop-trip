class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float | int
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_ride_cost(
            self,
            distance: int | float,
            fuel_price: int | float
    ) -> int | float:
        return ((self.fuel_consumption / 100) * distance) * fuel_price
