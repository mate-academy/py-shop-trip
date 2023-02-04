class Car:

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_cost_of_trip(self, distance: float, fuel_price: float) -> float:
        return round(
            (self.fuel_consumption / 100 * distance * fuel_price) * 2,
            2
        )
