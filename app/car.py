import dataclasses
import math

from typing import Union, Any

from app.shop import Shop


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    @staticmethod
    def trip_cost(
            shop: Shop,
            customer: Any,
            fuel_price: float
    ) -> Union[int, float]:

        distance = math.sqrt(
            (shop.location[0] - customer.location[0]) ** 2
            + (shop.location[1] - customer.location[1]) ** 2
        )

        total_trip_cost = round(
            (((distance / 100)
              * customer.car.fuel_consumption
              * fuel_price) * 2), 2
        )

        return total_trip_cost
