class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self, distance: int, fuel_price: float = 2.4) -> float:
        return round(distance / self.fuel_consumption * fuel_price, 2)
