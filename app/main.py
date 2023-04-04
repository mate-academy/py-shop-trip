import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from app.customer import Customer
from app.shop import Shop


@dataclass
class Config:
    customers: list[Customer]
    shops: list[Shop]
    fuel_price: float


def load_config() -> Config:
    path_json = Path(__file__).parent.joinpath("config.json")
    with open(path_json, "r") as file_info:
        data = json.load(file_info)
    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]
    return Config(customers, shops, fuel_price)


def shop_trip() -> Any:
    config = load_config()
    shops = config.shops
    for customer in config.customers:
        print(f"{customer.name} has {round(customer.money, 2)} dollars")
        shop_road_cost: dict[Shop, float] = {}
        for shop in shops:
            total = customer.get_cost_to_shop(shop, config.fuel_price)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name}" f" costs {round(total, 2)}"
            )
            shop_road_cost[shop] = total
        cheapest_shop = min(shop_road_cost, key=shop_road_cost.get)
        money_spend = shop_road_cost.get(cheapest_shop)
        if cheapest_shop and customer.money >= money_spend:
            customer.make_purchase(cheapest_shop, config.fuel_price)
        else:
            print(
                f"{customer.name} doesn't have enough money"
                " to make purchase in any shop"
            )
