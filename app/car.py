from app.utils import clean_round


class Car:
    FUEL_PRICE = 0

    def __init__(
            self,
            brand: str,
            fuel_consumption: int | float,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_consumption_cost(
            self,
            distance: int | float,
    ) -> int | float:
        return clean_round(
            self.fuel_consumption / 100 * distance * Car.FUEL_PRICE
        )
