import dataclasses

from app.shop_trip_moduls.Cars import Car
from app.shop_trip_moduls.Locations import Point


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: Point
    money: float
    car: Car
