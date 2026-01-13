"""Module for representing locations and cars for navigation."""
from dataclasses import dataclass
import math
from decimal import Decimal


@dataclass
class Location:
    """Represents a location with x and y coordinates."""

    x_coord: int = 0
    y_coord: int = 0

    def get_distance(self, other: "Location") -> Decimal:
        """
        Calculate the distance to another location.

        :param other: The other location.
        :type other: Location
        :return: The distance between the two locations.
        :rtype: Decimal
        """
        return Decimal(str(math.hypot(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord
        )))


@dataclass
class Car:
    """Represents a car with a brand and fuel consumption."""

    brand: str
    fuel_consumption: Decimal

    def get_trip_cost(
            self,
            fuel_price: Decimal,
            distance: Decimal
    ) -> Decimal:
        """
        Calculate the cost of a trip.

        :param fuel_price: The price of fuel.
        :type fuel_price: Decimal
        :param distance: The distance of the trip.
        :type distance: Decimal
        :return: The cost of the trip.
        :rtype: Decimal
        """
        return (
            self.fuel_consumption / 100 * fuel_price * distance
        )
