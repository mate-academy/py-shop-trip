class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def trip_cost(self, distance: float, fuel_price: float) -> float:
        return self.fuel_consumption * distance / 100 * fuel_price
