class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_costs(
        self, distance_covered: float, fuel_price: float
    ) -> float:
        fuel_consumed = distance_covered * 2 / 100 * self.fuel_consumption
        return round(fuel_consumed * fuel_price, 2)
