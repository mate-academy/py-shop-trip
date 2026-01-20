class Car:
    def __init__(self, fuel_price: float,
                 brand: str, fuel_consumption: float) -> None:
        self.fuel_price = fuel_price
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel(self, distance: float) -> float:
        return self.fuel_price * self.fuel_consumption / 100 * distance * 2
