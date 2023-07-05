from dataclasses import dataclass

from app.shop import Shop


@dataclass
class ChosenShop:
    total_trip_cost: int
    shopping_cost: int = None
    one_way_trip_cost: int = None
    shop: Shop = None
