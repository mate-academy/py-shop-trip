import json
import math
import datetime


def shop_trip():

    with open("app/config.json") as file_open:
        dict_shopping = json.load(file_open)

    fuel_price = dict_shopping["FUEL_PRICE"]
    customers_list = dict_shopping["customers"]
    shops_list = dict_shopping["shops"]

    for customer in customers_list:
        name = customer['name']
        cash = customer['money']
        print(f"{name} has {cash} dollars")

        dict_product = {}
        total_cost = {}

        for shop in shops_list:
            shop_name = shop["name"]

            distance = math.dist(customer["location"], shop["location"])
            fuel_consumption = customer["car"]["fuel_consumption"]
            price_trip = fuel_consumption / 100 * distance * fuel_price

            product_cost = {
                f"{customer['product_cart'][key]} {key}s":
                    customer["product_cart"][key] * values
                for key, values in shop["products"].items()}

            costs_shop = round(2 * price_trip + sum(product_cost.values()), 2)
            dict_product[shop_name] = {"product": product_cost}
            total_cost[shop_name] = costs_shop

            print(f"{name}'s trip to the {shop_name} costs {costs_shop}")

        if cash - min(total_cost.values()) > 0:
            cheap_shop = min(total_cost, key=total_cost.get)
            print(f"{name} rides to {cheap_shop}\n")

            time_now = datetime.datetime.now()
            time = time_now.strftime("%d/%m/%Y %H:%M:%S")
            print(
                f"Date: {time}\n"
                f"Thanks, {name}, for you purchase!\n"
                f"You have bought: "
            )

            product_cheap_shop = dict_product[cheap_shop]["product"]
            for product, price in product_cheap_shop.items():
                print(f"{product} for {price} dollars")

            print(
                f"Total cost is {sum(product_cheap_shop.values())} dollars\n"
                f"See you again!\n\n"
                f"{name} rides home\n"
                f"{name} now has {cash - total_cost[cheap_shop]} dollars\n"
            )

        else:
            print(
                f"{name} doesn't have enough "
                f"money to make purchase in any shop"
            )
