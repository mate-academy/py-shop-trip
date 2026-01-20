class Car:
    FUEL_PRICE = 2.4

    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
