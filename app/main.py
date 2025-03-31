import os
import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    direct = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(direct, "config.json")
    with open(path, "r") as json_file:
        config = json.load(json_file)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = [Shop(shop) for shop in config["shops"]]

    for person in customers:
        customer = Customer(person)
        print(f"{customer.name} has {customer.money} dollars")

        costs = {}
        for shop in shops:
            trip_cost = customer.car.trip_cost(customer.location,
                                               shop,
                                               fuel_price)
            products_cost = shop.products_cost(customer.product_cart)
            total_cost = trip_cost + products_cost
            costs[shop] = total_cost

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost}")

        best_shop = min(costs, key=costs.get)
        best_cost = costs[best_shop]

        if customer.money < best_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {best_shop.name}\n")
        customer.location = best_shop.location

        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        best_shop.buy(customer.product_cart)

        print(f"{customer.name} rides home")
        customer.location = person["location"]
        customer.money -= best_cost
        print(f"{customer.name} now has {customer.money} dollars\n")
