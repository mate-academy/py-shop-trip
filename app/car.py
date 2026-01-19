class Car:
    def __init__(self, car: dict[str, float]) -> None:
        self.brand = car.get("brand")
        self.fuel_consumption = car.get("fuel_consumption")
