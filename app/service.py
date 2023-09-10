from __future__ import annotations

import json
from math import sqrt
from app.shop import Shop
from app.customer import Customer


def read_data_from_file() -> list[dict]:
    with open("app/config.json", "r") as data_file:
        return json.load(data_file)


def fuel_data() -> float:
    return read_data_from_file().get("FUEL_PRICE")


def customer_data() -> list[Customer]:
    return Customer.customer_object(read_data_from_file().get("customers"))


def shop_data() -> list[Shop]:
    return Shop.shop_object(read_data_from_file().get("shops"))


def distance(
        customer_location: list,
        shop_location: list
) -> float:
    x1, y1 = customer_location
    x2, y2 = shop_location
    return (
        sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) * 2
    )
