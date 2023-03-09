class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        self.__brand = brand
        self.__fuel_consumption = fuel_consumption
        self.__fuel_price = fuel_price

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def fuel_consumption(self) -> float:
        return self.__fuel_consumption

    @property
    def fuel_price(self) -> float:
        return self.__fuel_price
