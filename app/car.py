class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        self.__brand = brand
        self.__fuel_price_per_1_km = fuel_consumption / 100 * fuel_price

    @property
    def get_fuel_price_per_1_km(self) -> float:
        return self.__fuel_price_per_1_km
