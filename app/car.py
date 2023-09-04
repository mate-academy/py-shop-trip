from dataclasses import dataclass
import math


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculation_of_road_costs(
            self,
            location_customer: list,
            location_shop: list,
            fuel_price: float
    ) -> float:
        distance_to_the_store = math.sqrt(
            ((location_shop[0] - location_customer[0]) ** 2)
            + ((location_shop[1] - location_customer[1]) ** 2)
        )
        fuel_expenses = (distance_to_the_store / 100 * self.fuel_consumption
                         * fuel_price) * 2
        return round(fuel_expenses, 2)
