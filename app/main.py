import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_path) as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_trip = {"shop": None, "total_cost": float('inf'), "fuel_cost": 0, "product_cost": 0}

        for shop in shops:
            total_cost, fuel_cost, product_cost = customer.calculate_trip_total(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost:.2f}")

            if total_cost < best_trip["total_cost"]:
                best_trip.update({
                    "shop": shop,
                    "total_cost": total_cost,
                    "fuel_cost": fuel_cost,
                    "product_cost": product_cost
                })

        if best_trip["total_cost"] <= customer.money:
            customer.go_shopping(best_trip["shop"], best_trip["fuel_cost"], best_trip["product_cost"])
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
