class Car:
    def __init__(self, car: dict) -> None:
        self.brand: str = car.get("brand")
        self.fuel_consumption: float = car.get("fuel_consumption")
