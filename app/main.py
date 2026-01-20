import json

from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config = json.load(config)
        for customer in config["customers"]:
            res = {}
            print(f"{customer['name']} has {customer['money']} dollars")

            for shop in config["shops"]:

                trip_cost = Car(
                    config["FUEL_PRICE"],
                    customer["car"]["fuel_consumption"],
                    customer["location"], shop["location"]
                ).calculate_trip_cost()

                products_price = Shop(
                    customer["name"],
                    customer["product_cart"],
                    shop["products"]
                ).calculate_total_price()

                res[trip_cost + products_price] = [
                    {"customer_name": customer["name"]},
                    {"products": customer["product_cart"]},
                    {"products_in_shop": shop["products"]},
                    {"shop_name": shop["name"]},
                    {"shop_location": shop["location"]}
                ]

                print(f"{customer['name']}'s trip to the "
                      f"{shop['name']} costs {trip_cost + products_price}")

            if customer["money"] < min(res.keys()):
                print(f"{customer['name']} doesn't have enough "
                      f"money to make a purchase in any shop")
                continue
            customer_home_location = customer["location"]
            print(f"{customer['name']} rides to "
                  f"{res[min(res)][-2]['shop_name']}\n")
            customer["location"] = res[min(res)][-1]["shop_location"]

            Shop(
                res[min(res)][0]["customer_name"],
                res[min(res)][1]["products"],
                res[min(res)][2]["products_in_shop"]
            ).print_account()

            print(f"{customer['name']} rides home")
            customer["location"] = customer_home_location
            print(f"{customer['name']} now has "
                  f"{customer['money'] - min(res.keys())} dollars\n")
