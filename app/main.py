import datetime
import json
import math


def shop_trip():
    with open("app/config.json") as file_read:
        dict_info = json.load(file_read)

    for customer in dict_info["customers"]:
        name = customer["name"]
        cash_value = customer["money"]
        print(f"{name} has {cash_value} dollars")

        dict_shop = {}
        total_price = {}
        time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#   Count price to shop by car
        for shop in dict_info["shops"]:
            shop_name = shop["name"]
            distance_to_shop = math.dist(customer["location"],
                                         shop["location"])
            trip_price = customer["car"]["fuel_consumption"] / 100 * \
                distance_to_shop * dict_info["FUEL_PRICE"]

# Count price for products Customer and Shop
            products_cost = {
                f"{customer['product_cart'][key]} {key}s":
                    customer["product_cart"][key] * value
                for key, value in shop["products"].items()
            }
            total_trip_shop = round(
                trip_price * 2 + sum(products_cost.values()), 2)
            dict_shop[shop_name] = {"product": products_cost}
            total_price[shop_name] = total_trip_shop

            print(f"{name}'s trip to the {shop_name} costs {total_trip_shop}")

# chose the cheapest SHOP and print info
        if cash_value - min(total_price.values()) > 0:
            cheapest_shop = min(total_price, key=total_price.get)
            print(f"{name} rides to {cheapest_shop}\n")

# Date format
            print(
                f"Date: {time_now}\n"
                f"Thanks, {name}, for you purchase!\n"
                f"You have bought: "
            )
# print purchase info
            cheapest_shop_products = dict_shop[cheapest_shop]["product"]
            for product, price in cheapest_shop_products.items():
                print(f"{product} for {price} dollars")

# finally, total price
            print(
                f"Total cost is "
                f"{sum(cheapest_shop_products.values())} dollars\n"
                f"See you again!\n"
            )
# back home, count money
            print(
                f"{name} rides home\n"
                f"{name} now has "
                f"{cash_value - total_price[cheapest_shop]} dollars\n"
            )
        else:
            print(f"{name} doesn't have enough money "
                  f"to make purchase in any shop")
