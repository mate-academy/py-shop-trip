class Car:
    def __init__(self,
                 brand: str = "Unknown",
                 fuel_consumption: int = 0) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
