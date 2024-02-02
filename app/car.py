from decimal import Decimal


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = Decimal(str(fuel_consumption))
