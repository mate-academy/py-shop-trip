import os
import json
from decimal import Decimal

from .shop import Shop, NoProductException
from .customer import Customer


def shop_trip() -> None:
    this_directory = os.path.dirname(__file__)
    config_filename = os.path.join(this_directory, "config.json")

    with open(config_filename) as config_file:
        config = json.load(config_file)

    fuel_price = Decimal(config["FUEL_PRICE"])
    customers = [Customer.from_dict(d) for d in config["customers"]]
    shops = [Shop.from_dict(d) for d in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        possible_trips = {}
        for shop in shops:
            try:
                trip_cost = customer.get_full_trip_cost(shop, fuel_price)
            except NoProductException as e:
                print(f"{shop.name} has no product {e.args[0]!r}")
            else:
                print(
                    f"{customer.name}'s trip to the {shop.name}"
                    f" costs {round(trip_cost, 2)}"
                )
                possible_trips[trip_cost] = shop
        if not possible_trips:
            print(f"{customer.name} did not find a suitable shop")
        else:
            min_cost = min(possible_trips)
            if min_cost > customer.money:
                print(
                    f"{customer.name} doesn't have enough money"
                    " to make a purchase in any shop"
                )
            else:
                shop = possible_trips[min_cost]
                customer.visit_shop(shop, fuel_price)
                print(
                    f"{customer.name} now has"
                    f" {round(customer.money, 2)} dollars\n"
                )


if __name__ == "__main__":
    shop_trip()
