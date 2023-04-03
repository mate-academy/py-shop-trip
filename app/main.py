import json
<<<<<<< HEAD
from dataclasses import dataclass
from typing import Any
=======
>>>>>>> fdd224fdc68e73fd0dc447ddb5a6bcbbf20eca65
from pathlib import Path
from typing import Any

from app.shop import Shop
from app.customer import Customer


@dataclass
class Config:
    customers: list[Customer]
    shops: list[Shop]
    fuel_price: float


def load_config() -> Config:
    path_json = Path(__file__).parent.joinpath("config.json")
    with open(path_json, "r") as file_info:
        data = json.load(file_info)
    customers = [customer for customer in data["customers"]]
    shops = [shop for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]
    return Config(customers, shops, fuel_price)


def get_min_purchase_price(customer: Customer, shops: list[Shop]) -> float:
    min_purchase_price = []
    for shop in shops:
        purchase_price = shop.products["products"]\
            * customer.product_cart["product_cart"]
        min_purchase_price.append(purchase_price)
    return min(min_purchase_price)


def shop_trip() -> Any:
    config = load_config()
    for customer in config.customers:
        total_cost_products = customer.get_min_purchase_price
        total = total_cost_products + customer.get_fare * 2
        print(
            f"{customer} has {customer.money} dollars\n"
            f"{customer}'s trip to the {shop.name}"
            f" costs {total}\n"
            f"{customer}'s trip to the {shop.name}"
            f" costs {total}\n"
            f"{customer} rides to {shop.name}"
        )
        if customer.money >= total:
            print(
                f"{customer.name} rides home\n"
                f"{customer.name} has {customer.money - total} dollars"
            )
        else:
            print(
                f"{customer.name} has {customer.money} dollars\n"
                f"{customer.name} trip to the {shop.name}"
                f" costs {total}\n"
                f"{customer.name} trip to the {shop.name}"
                f" costs {total}\n"
                f"{customer.name} doesn't have enough money"
                "to make purchase in any shop"
            )
