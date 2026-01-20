from math import sqrt


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def liters_needed(
            self,
            customer_location: list,
            shop_location: list
    ) -> float:
        distance_to_shop = (sqrt(
            (shop_location[0] - customer_location[0]) ** 2
            + (shop_location[1] - customer_location[1]) ** 2)
            * 2)
        liters_needed = self.fuel_consumption / 100 * distance_to_shop
        return liters_needed
