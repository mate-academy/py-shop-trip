import json
import dataclasses
from typing import List


@dataclasses.dataclass
class Person:
    name: str
    location: List[int]
    money: int | float
    car_brand: str
    fuel_consumption: float | int
    product: dict
    fuel_price: int | float


with open("app/config.json", "r") as file:
    data = json.load(file)
    customers = data["customers"]
    fuel_price = data["FUEL_PRICE"]

persons = []

for person in customers:
    one_person = (
        Person(person["name"],
               person["location"],
               person["money"],
               person["car"]["brand"],
               person["car"]["fuel_consumption"],
               person["product_cart"],
               fuel_price)
    )
    persons.append(one_person)
