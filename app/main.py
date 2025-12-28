import json
from pathlib import Path

from app.config.config import Config
from app.config.exception import EmptyConfigException


def shop_trip() -> None:
    path_config = str(Path(__file__).resolve().parent) + "/config.json"
    config: Config = get_configs(path_config)
    for customer in config.customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_cost = {}
        for shop in config.shops:
            cost_fuel = config.get_cost_fuel(customer, shop)
            costs_in_shop = shop.get_total_costs(customer)
            full_cost = round(cost_fuel + costs_in_shop, 2)
            if full_cost <= customer.money:
                trip_cost[shop] = full_cost
            print(
                f"{customer.name}'s trip to "
                f"the {shop.name} costs {full_cost}"
            )

        if len(trip_cost) == 0:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue

        cheap_shop = min(trip_cost, key=trip_cost.get)
        print(f"{customer.name} rides to {cheap_shop.name}")
        cheap_shop.print_purchase_for_customer(customer)
        customer.money = round(customer.money - trip_cost[cheap_shop], 2)

        print(
            "\n"
            f"{customer.name} rides home\n"
            f"{customer.name} now has {customer.money} dollars"
            "\n"
        )


def get_configs(file_name: str) -> Config:
    try:
        with open(file_name, "r") as config_file:
            config_dict = json.load(config_file)
    except FileNotFoundError:
        raise

    if not config_dict:
        raise EmptyConfigException("Config can not be empty")

    return Config(config_dict)
