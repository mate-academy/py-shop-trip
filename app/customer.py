import dataclasses
from typing import List
from app.data_jason import load_json


@dataclasses.dataclass
class Person:
    name: str
    location: List[int]
    money: int | float
    car_brand: str
    fuel_consumption: float | int
    product: dict
    fuel_price: int | float

    @classmethod
    def load_person(cls) -> list["Person"]:
        data = load_json(filename="app\\config.json")
        # noinspection PyUnresolvedReferences
        customers = data["customers"]
        # noinspection PyUnresolvedReferences
        fuel_price = data["FUEL_PRICE"]

        persons = []

        for person in customers:
            new_person = cls(
                person["name"],
                person["location"],
                person["money"],
                person["car"]["brand"],
                person["car"]["fuel_consumption"],
                person["product_cart"],
                fuel_price,
            )
            persons.append(new_person)

        return persons
