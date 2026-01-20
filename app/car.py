class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def fuel_costs(self, distance: float, price: float) -> float:
        return (self.fuel_consumption / 100 * distance) * price
