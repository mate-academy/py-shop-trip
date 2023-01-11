class Car:
    def __init__(
            self,
            brand: str,
            consumption: float,
            fuel_price: float
    ) -> None:
        self.brand = brand
        self.consumption = consumption
        self.fuel_price = fuel_price
