from decimal import Decimal


class Car:
    def __init__(
            self,
            fuel_price: float,
            brand: str,
            consumption: Decimal
    ) -> None:
        self.fuel_price = Decimal(fuel_price)
        self.brand = brand
        self.consumption = consumption
