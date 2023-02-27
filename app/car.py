from __future__ import annotations

from app.location import Location


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self._brand = brand
        self._fuel_consumption = fuel_consumption

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    def __repr__(self) -> str:
        return f"{self.brand} with fuel consumption {self.fuel_consumption}"

    @classmethod
    def car_from_dict(cls, car_info: dict) -> Car:
        return cls(
            brand=car_info.get("brand"),
            fuel_consumption=car_info.get("fuel_consumption")
        )

    def estimate_trip_price(
        self,
        price: float,
        cur_location: Location,
        dest_location: Location
    ) -> float:
        distance = cur_location.get_distance(dest_location)
        return round((distance * (self.fuel_consumption / 100) * price) * 2, 2)
