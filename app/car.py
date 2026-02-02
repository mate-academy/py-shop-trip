from decimal import Decimal


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: Decimal
                 ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
