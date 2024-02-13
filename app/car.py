class Car:
    def __init__(self, brand: str, fuel_consumtion: float) -> None:
        self.brand = brand
        self.fuel_consumtion = fuel_consumtion

    def get_fuel_consum_for_km(self) -> float:
        return self.fuel_consumtion / 100
