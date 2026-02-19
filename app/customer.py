from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from .car import Car
from .shop import Shop
from .utils import Location, euclidean_distance_km


@dataclass
class Customer:
    """Customer that can choose a shop and perform a shopping trip."""

    name: str
    product_cart: Dict[str, int]
    location: Location
    money: float
    car: Car

    def trip_cost_to_shop(
        self,
        shop: Shop,
        fuel_price: float,
    ) -> Optional[float]:
        """
        Calculate total trip cost to a shop.

        total = fuel_to_shop + products_cost + fuel_to_home
              = 2 * fuel_one_way + products_cost
        """
        if not shop.can_fulfill_cart(self.product_cart):
            return None

        distance_one_way = euclidean_distance_km(self.location, shop.location)
        fuel_one_way = self.car.fuel_cost_for_distance(
            distance_one_way,
            fuel_price,
        )
        products_cost = shop.cart_cost(self.product_cart)
        total_cost = (2.0 * fuel_one_way) + products_cost
        return total_cost

    def choose_cheapest_shop(
        self,
        shops: Tuple[Shop, ...],
        fuel_price: float,
    ) -> Tuple[Optional[Shop], Optional[float]]:
        """Return cheapest shop and its total trip cost."""
        cheapest_shop: Optional[Shop] = None
        cheapest_cost: Optional[float] = None

        for shop in shops:
            total_cost = self.trip_cost_to_shop(shop, fuel_price)
            if total_cost is None:
                continue

            if cheapest_cost is None or total_cost < cheapest_cost:
                cheapest_cost = total_cost
                cheapest_shop = shop

        return cheapest_shop, cheapest_cost

    def perform_purchase_trip(self, shop: Shop, total_cost: float) -> None:

        home_location = self.location

        self.location = shop.location
        shop.print_receipt(self.name, self.product_cart)

        self.money -= total_cost
        self.location = home_location
