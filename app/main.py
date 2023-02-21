from __future__ import annotations

import json

from app.customer import Customer
from app.shop import Shop
from app.logic_functions import start_trip


def shop_trip() -> None:
    with open("app/config.json", "r") as file_in:
        data = json.load(file_in)
        fuel_price = data.get("FUEL_PRICE")
        shops = Shop.shops_maker(data.get("shops"))
        customers = Customer.customers_maker(data.get("customers"))
        start_trip(customers, shops, fuel_price)
