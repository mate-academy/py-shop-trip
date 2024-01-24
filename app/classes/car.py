class Car:
    def __init__(
            self,
            model: str,
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
