class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_price(
            self,
            distance: float,
            fuel_price: int,
    ) -> float:

        fuel_cost = (self.fuel_consumption / 100) * distance * fuel_price

        return fuel_cost
