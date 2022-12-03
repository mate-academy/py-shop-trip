from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.shop import Shop
    from app.customer import Customer

"""
TYPE_CHECKING from the "typing" module has been imported
and the "if TYPE_CHECKING" condition has been implemented
to provide for type annotations for the "customer" and "shop" parameters
of the "fuel_cost" method without cyclic imports
"""


class Car:

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> float:
        distance = ((customer.location[0] - shop.location[0]) ** 2
                    + (customer.location[1] - shop.location[1]) ** 2) ** 0.5
        fuel_cost = distance * self.fuel_consumption * fuel_price / 100
        return fuel_cost
