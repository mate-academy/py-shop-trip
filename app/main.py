from __future__ import annotations
import json
from typing import Any

from app.shops import Shop
from app.customers import Customer


def unpack() -> Any:
    with open("app/config.json", "r") as config_file:
        config_dict = json.load(config_file)
        customers = [
            Customer(customer) for customer in config_dict["customers"]
        ]
        shops = [Shop(shop) for shop in config_dict["shops"]]
        Shop.FUEL_PRICE = config_dict["FUEL_PRICE"]
        return customers, shops


def shop_trip() -> None:
    customers, shops = unpack()
    for customer in customers:
        shop = customer.choose_shop(shops)
        if shop is not None:
            shop.purchase_receipt(customer)
            customer.back_home()
