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
    BASE_DIR = os.path.dirname(__file__)
    config_path = os.path.join(BASE_DIR, "config.json")

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

    for c in customers:
        # line with customer's money
        print(f"{c.name} has {round(c.money, 2)} dollars")

        total_cost = []
        # compute and print trip costs (note: include "the " before shop name)
        for shop in shops:
            raw_cost = c.calculate_trip_cost(shop, fuel_price=config["FUEL_PRICE"])
            cost = round(raw_cost, 2)
            print(f"{c.name}'s trip to the {shop.name} costs {cost}")
            total_cost.append((shop, cost))

        # choose cheapest
        cheapest_shop, cheapest_cost = min(total_cost, key=lambda x: x[1])

        if c.money >= cheapest_cost:
            # rides to (NO "the" here) — test expects "Bob rides to Outskirts Shop"
            print(f"{c.name} rides to {cheapest_shop.name}\n")

            # go to shop, print receipt with fixed date format
            start_location = c.location.copy()
            c.location = cheapest_shop.location

            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"Date: {now}")
            cheapest_shop.print_check(c.name, c.cart)

            # subtract cost and return home
            c.money -= cheapest_cost
            c.location = start_location

            print(f"\n{c.name} rides home")
            print(f"{c.name} now has {round(c.money, 2)} dollars\n")
        else:
            print(f"{c.name} doesn't have enough money to make a purchase in any shop")

#  if __name__ == "__main__":
#    shop_trip()
