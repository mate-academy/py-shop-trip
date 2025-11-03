import json
import os
import datetime
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    """
    Simulate a shop trip.
    """
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    shops = [Shop(
        name=s["name"],
        location=s["location"],
        products=s["products"]
    ) for s in config["shops"]]
    customers = [Customer(
        name=c["name"],
        cart=c["product_cart"],
        location=c["location"],
        money=c["money"],
        car=Car(
            brand=c["car"]["brand"],
            fuel_consumption=c["car"]["fuel_consumption"]
        )
    ) for c in config["customers"]]

    for customer in customers:
        # line with customer's money
        print(f"{customer.name} has {round(customer.money, 2)} dollars")

        total_cost = []
        # compute and print trip costs
        # (note: include "the " before shop name)
        for shop in shops:
            raw_cost = (customer.calculate_trip_cost
                        (shop, fuel_price=config["FUEL_PRICE"]))
            cost = round(raw_cost, 2)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            total_cost.append((shop, cost))

        # choose cheapest
        cheapest_shop, cheapest_cost = min(total_cost, key=lambda x: x[1])

        if customer.money >= cheapest_cost:
            # rides to (NO "the" here) — test expects
            # "Bob rides to Outskirts Shop"
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            # go to shop, print receipt with fixed date format
            start_location = customer.location.copy()
            customer.location = cheapest_shop.location

            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"Date: {now}")
            cheapest_shop.print_check(customer.name, customer.cart)

            # subtract cost and return home
            customer.money -= cheapest_cost
            customer.location = start_location

            print(f"\n{customer.name} rides home")
            print(f"{customer.name} "
                  f"now has {round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
