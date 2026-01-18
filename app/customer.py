from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict
from app.car import Car


@dataclass
class Customer:
    name: str
    location: list
    money: int
    product_cart: dict
    car: Car
    home_location: list

    price_of_products: Dict[str, Dict[str, Decimal]] \
        = field(default_factory=dict)
    total_price: Dict[str, int] = field(default_factory=dict)
    fuel_sum: Dict[str, float] = field(default_factory=dict)
    total_trip_cost: Dict[str, Decimal] = field(default_factory=dict)
    cheapest_shop: str = field(default_factory=str)
    cheapest_cost: Decimal = field(default_factory=float)
