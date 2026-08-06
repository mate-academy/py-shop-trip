import json
import datetime
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "config.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    fuel_price = float(data["FUEL_PRICE"])

    customers = [Customer(c["name"],
                          c["product_cart"],
                          c["location"],
                          c["money"],
                          c["car"]) for c in data["customers"]]
    shops = [Shop(s["name"],
                  s["location"],
                  s["products"]) for s in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {int(customer.money)} dollars")

        best_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            trip_cost = customer.evaluate_trip(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")

            if trip_cost < min_trip_cost:
                min_trip_cost = trip_cost
                best_shop = shop

        if customer.money >= min_trip_cost:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.ride_to_shop(best_shop)
            formatted_date = (
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            best_shop.print_receipt(customer.name,
                                    customer.product_cart,
                                    formatted_date)

            print(f"{customer.name} rides home")
            customer.money = round(customer.money - min_trip_cost, 2)
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't "
                  f"have enough money to make a purchase in any shop")
