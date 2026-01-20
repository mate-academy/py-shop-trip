import math

from app.customer import Customer
from app.shop import Shop


class Car:

    cars_dict = {}

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def distance_to_shop(
            self,
            customer: Customer,
            data: dict,
            some_shop: Shop
    ) -> float:
        fuel_cost = data.get("FUEL_PRICE")

        distance_c = customer.location
        distance_sh = some_shop.location
        distance = round(
            (math.sqrt(
                (
                    (distance_sh[0] - distance_c[0]) ** 2
                ) + (
                    (distance_sh[1] - distance_c[1]) ** 2
                )
            ) * 2
            ),
            2
        )
        cost_trip = round(
            ((distance * self.fuel_consumption) / 100) * fuel_cost,
            2
        )

        return cost_trip
