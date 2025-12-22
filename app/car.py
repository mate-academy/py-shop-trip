class CarInfo:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float,
                 fuel_price: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price_per_km = (fuel_consumption / 100) * fuel_price
