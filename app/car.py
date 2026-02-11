from __future__ import annotations
import math
from typing import ClassVar
from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer
    from app.shop import Shop


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    fuel_price: ClassVar[float] = 0.0

    def ride_to(self, owner: Customer, location: Shop | None = None) -> str:
        if location is None:
            print(f"{owner.name} rides home")
            return f"{owner.name} now has {owner.money:.2f} dollars"
        trip_cost = (
            self.trip_fuel_consumption(owner.location, location.location)
        )
        owner.money -= trip_cost
        return f"{owner.name} rides to {location.name}"

    def trip_fuel_consumption(
            self,
            start_coord: tuple,
            end_coord: tuple
    ) -> float:
        distance_km = math.sqrt(
            (end_coord[0] - start_coord[0]) ** 2
            + (end_coord[1] - start_coord[1]) ** 2
        )
        travel_price = ((distance_km * (self.fuel_consumption / 100))
                        * self.fuel_price)
        travel_price *= 2
        return round(travel_price, 2)
