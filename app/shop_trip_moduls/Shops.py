import dataclasses

from app.shop_trip_moduls.Locations import Point


@dataclasses.dataclass
class Shop:
    name: str
    _location: Point
    price_list: dict

    def get_location(self) -> Point:
        return self._location
