from __future__ import annotations
from app.store import Shop
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculating_ride_cost(
            self,
            distance: int | float,
            fuel_price: int | float
    ) -> int | float:
        return ((distance * (self.fuel_consumption / 100)) * fuel_price) * 2

    @staticmethod
    def drive(owner: Customer, destination: Shop | list) -> None:
        print(f"{owner.name} rides to {destination.name}\n")
        owner.current_location = destination.location

    @staticmethod
    def drive_home(owner: Customer) -> None:
        print(f"{owner.name} rides home")
        owner.current_location = owner.current_location
