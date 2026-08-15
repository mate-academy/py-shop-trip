class Car:
    def __init__(self, brand: str, fuel_consumption: float | int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(
            self,
            distance: float | int,
            fuel_price: float
    ) -> float:
        return distance * self.fuel_consumption / 100 * fuel_price
