class Car:
    def __init__(self, car: dict) -> None:
        self.name = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def calculate_fuel_price(
            self,
            fuel_price: float | int,
            distance: float | int
    ) -> float:
        return distance / 100 * fuel_price * self.fuel_consumption
