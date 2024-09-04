class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: int | float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def one_km_consumption(self) -> float:
        return self.fuel_consumption / 100
