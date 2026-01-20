class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __repr__(self) -> str:
        return f"{self.brand}, {self.fuel_consumption}"
