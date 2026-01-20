class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: int | float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @property
    def fuel_consumption_for_one_km(self) -> int | float:
        return self.fuel_consumption / 100
