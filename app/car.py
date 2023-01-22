class Car:
    def __init__(self, car: dict[str, str | int | float]) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def calculate_fuel_needed_for_trip(
            self,
            distance: int | float
    ) -> int | float:
        return self.fuel_consumption * distance / 100
