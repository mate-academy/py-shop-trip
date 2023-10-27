from dataclasses import dataclass

from app.shop import Shop


@dataclass
class ChosenShop:
    total_trip_cost: float
    shopping_cost: float
    one_way_trip_cost: float
    shop: Shop
