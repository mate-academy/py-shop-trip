from app.constant import FUEL_PRICE
import math


class Car:
    def __init__(self, brand: int, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_trip(self,
                  customer_location: list[int],
                  shop_location: list[int]) -> float:
        distance = math.sqrt(
            (shop_location[0] - customer_location[0]) ** 2
            + (shop_location[1] - customer_location[1]) ** 2
        )
        return self.fuel_consumption * distance / 100 * FUEL_PRICE
