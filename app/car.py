class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def trip_cost(self, distance: float, fuel_price: float) -> float:
        return (self.fuel_consumption / 100 * distance) * fuel_price
