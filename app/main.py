import os

from app.config_loader import config_loader
from app.models import Customer, Shop


def shop_trip() -> None:
    path = os.path.dirname(__file__) + "/config.json"
    config = config_loader(path)

    fuel_price = config.get("FUEL_PRICE", 0)

    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        cheapest_shop = None
        cheapest_cost = float("inf")
        print(f"{customer.name} has {customer.money} dollars")

        for index, shop in enumerate(shops):
            trip_cost = customer.calc_trip_cost(shop, fuel_price)
            print_trip = (
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            print(print_trip)

            if trip_cost < cheapest_cost and trip_cost <= customer.money:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.print_check(cheapest_shop)
            customer.money -= cheapest_cost
            customer.ride_home()
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
