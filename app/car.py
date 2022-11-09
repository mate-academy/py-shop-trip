class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def car_fuel_costs(self, fuel_price: float, distance: float) -> float:
        return (self.fuel_consumption / 100 * distance) * fuel_price
