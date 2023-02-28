FUEL_PRICE = 2.4


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __str__(self) -> str:
        return (f"Car(brand={self.brand}, "
                f"fuel_consumption={self.fuel_consumption})")

    @property
    def fuel_consumption_in_km(self) -> float:
        return self.fuel_consumption / 100
