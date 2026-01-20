import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_price(
            self,
            customer_location: list,
            shop_location: list,
            fuel_price: float
    ) -> float:
        distance = math.sqrt(
            ((customer_location[0] - shop_location[0]) ** 2)
            + ((customer_location[1] - shop_location[1]) ** 2)
        )
        fuel_per_kilometer = self.fuel_consumption / 100

        return (distance * fuel_per_kilometer * 2) * fuel_price
