import json

from typing import Dict, Any
from app.classes import Customer, Shop


def from_json() -> Dict[str, Any]:
    with open("app/config.json") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(*customer.values())
        for customer in data["customers"]
    ]
    shops = [Shop(*shop.values()) for shop in data["shops"]]
    return {
        "fuel_price": fuel_price,
        "customers": customers,
        "shops": shops
    }
