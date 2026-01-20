from dataclasses import dataclass

from app.customer import Customer
from app.shop import Shop


@dataclass
class Car:
    brand: str
    fuel_consumption: int | float

    def litres_per_trip(
            self,
            shop: Shop,
            customer: Customer
    ) -> int | float:
        distance = shop.calculate_trip_distance(customer)
        return (self.fuel_consumption * distance) / 100
