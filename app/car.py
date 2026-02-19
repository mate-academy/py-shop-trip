from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    """Car model used to calculate fuel costs."""

    brand: str
    fuel_consumption: float  # liters per 100 km

    def fuel_cost_for_distance(
        self,
        distance_km: float,
        fuel_price: float,
    ) -> float:
        """
       Return the fuel cost to drive a given distance.

        The fuel consumption is measured in liters per 100 km.
        """
        liters_spent: float = distance_km * (self.fuel_consumption / 100.0)
        return liters_spent * fuel_price
