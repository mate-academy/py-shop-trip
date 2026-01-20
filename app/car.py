from math import sqrt


class Car:
    fuel_price = None

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_cost_ride_to_shop(
        self, home_location: list[int, int], shop_location: list[int, int]
    ) -> int | float:

        return (
            sqrt(
                (home_location[0] - shop_location[0]) ** 2
                + (home_location[1] - shop_location[1]) ** 2
            )
            * (self.fuel_consumption / 100)
            * self.fuel_price
        )
