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
    def fuel_price_per_1_km(self) -> float:
        return self.__fuel_price_per_1_km

    @fuel_price_per_1_km.setter
    def fuel_price_per_1_km(self, fuel_price_per_1_km: float) -> None:
        if not isinstance(fuel_price_per_1_km, float):
            raise TypeError("Fuel price per 1 km for a car should be float")
        if fuel_price_per_1_km < 0:
            raise ValueError("Fuel price per 1 km for a car can't be negative")
        self.__fuel_price_per_1_km = fuel_price_per_1_km
