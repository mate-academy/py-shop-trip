import json
import os

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = [Customer(**customer_data) for customer_data in customers_data]

    shops = [Shop(**shop_data) for shop_data in shops_data]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = []
        for shop in shops:
            cost = customer.calculate_total_trip_cost(shop, fuel_price)
            trip_costs.append((cost, shop))
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost}")

        cheapest_trip = min(trip_costs)
        cheapest_cost, cheapest_shop = cheapest_trip

        if cheapest_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.make_trip(cheapest_shop, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


shop_trip()
