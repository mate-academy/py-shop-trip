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


def get_min_purchase_price(customer: Customer, shop: Shop) -> float:
    purchase_price = 0
    for product, amount in customer.product_cart.items():
        purchase_price += shop.products[product] * amount
    return purchase_price


def shop_trip() -> Any:
    config = load_config()
    shops = config.shops
    for customer in config.customers:
        print(f"{customer.name} has {round(customer.money, 2)} dollars")
        shop_road_cost = {}
        for shop in shops:
            products_cost = \
                get_min_purchase_price(customer=customer, shop=shop)
            cost_road = \
                customer.get_fare(shop=shop, fuel_price=config.fuel_price)
            total = products_cost + cost_road * 2
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name}" f" costs {round(total, 2)}"
            )
            shop_road_cost[shop.name] = total
        cheapest_shop = list(shop_road_cost.keys())[0]
        for shop_name, road_cost in shop_road_cost.items():
            if road_cost < shop_road_cost[cheapest_shop]:
                cheapest_shop = shop_name
        money_spend = shop_road_cost[cheapest_shop]
        if customer.money >= money_spend:
            print(f"{customer.name} rides to {cheapest_shop}\n")
            shop_object = shops[0]
            for shop_ in shops[1:]:
                if shop_.name == cheapest_shop:
                    shop_object = shop_
            print(shop_object.print_check(customer))
            print(
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{round(customer.money - money_spend, 2)} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money"
                " to make purchase in any shop"
            )
