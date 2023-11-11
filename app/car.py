class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
    ) -> str:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_trip_cost(
            self,
            distance: int,
            fuel_price: float
    ) -> float:
        cost_trip = (distance * (self.fuel_consumption / 100)) * fuel_price
        return cost_trip
