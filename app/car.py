class Car:
    def __init__(
        self,
        brand: str,
        fuel_consumption: int | float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
