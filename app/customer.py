from __future__ import annotations
from typing import List
from dataclasses import dataclass
from app.data_json import load_data


@dataclass
class Person:
    name: str
    product: dict
    location: List[float]
    money: int
    car_brand: str
    car_fuel_consumption: float
    fuel_price: float

    @classmethod
    def people_load(cls) -> List[Person]:
        data = load_data(filename="app/config.json")
        customers = data["customers"]
        fuel_price = data["FUEL_PRICE"]

        persons = [
            cls(
                person["name"],
                person["product_cart"],
                person["location"],
                person["money"],
                person["car"]["brand"],
                person["car"]["fuel_consumption"],
                fuel_price
            )
            for person in customers
        ]
        return persons
