class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_calculation(self, amount: float, fuel_price: float) -> float:
        return ((amount * self.fuel_consumption) / 100) * fuel_price
