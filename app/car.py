class Car:
    def __init__(self, car: dict) -> None:
        self.fuel_consumption = car["fuel_consumption"]

    def fuel_cost(self, distance: float, fuel_price: float | int) -> float:
        return (self.fuel_consumption / 100 * distance) * fuel_price
