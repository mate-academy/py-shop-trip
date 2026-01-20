import json
from os import path
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = path.join(path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_total_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")
            if trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                best_shop = shop

        if best_shop:
            customer.buy_products(best_shop, fuel_price)
