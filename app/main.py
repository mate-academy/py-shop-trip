from app.customer import Customer
from app.shop import Shop

import json

from math import sqrt
import datetime


def shop_trip() -> None:
    with open("app/config.json", "r") as read_file:
        data = json.load(read_file)

    fuel_price = data["FUEL_PRICE"]
    today = datetime.datetime.now()
    modified_today = today.strftime("%d/%m/%Y %H:%M:%S")

    customers_list = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"],
                 customer["car"])
        for customer in data["customers"]]

    shops_list = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in data["shops"]
    ]

    def product_cost() -> int or float:
        milk = customer.product_cart["milk"] * shop.products["milk"]
        breads = customer.product_cart["bread"] * shop.products["bread"]
        butters = customer.product_cart["butter"] * shop.products["butter"]
        return milk + breads + butters

    def trip_cost(x1: int, y1: int, x2: int, y2: int) -> float:
        location = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cost = location * fuel_price * customer.car["fuel_consumption"] / 100
        return round(cost * 2, 2) + product_cost()

    def info_after_shopping(remainder: int or float) -> str:
        return (f"{customer.name} rides home\n{customer.name}"
                f" now has {customer.money - remainder} dollars\n")

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        preferable_shop = [7777777, ""]
        for shop in shops_list:

            a1 = customer.location[0]
            b1 = customer.location[1]

            a2 = shop.location[0]
            b2 = shop.location[1]

            current_trip_cost = trip_cost(a1, b1, a2, b2)

            if current_trip_cost < preferable_shop[0]:
                preferable_shop[0] = current_trip_cost
                preferable_shop[1] = shop.name

            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {current_trip_cost}")

        if preferable_shop[0] < customer.money:
            print(f"{customer.name} rides to {preferable_shop[1]}\n")
            for market in shops_list:
                if str(market) == preferable_shop[1]:
                    customer_cart = customer.product_cart
                    print(f"Date: {modified_today}")
                    print(f"Thanks, {customer.name}, for you purchase!")
                    print("You have bought: ")

                    milk_cost = (market.products["milk"]
                                 * customer_cart["milk"])

                    bread_cost = (market.products["bread"]
                                  * customer_cart["bread"])

                    butter_cost = (market.products["butter"]
                                   * customer_cart["butter"])

                    print(f"{customer_cart['milk']} milks for "
                          f"{milk_cost} dollars")

                    print(f"{customer_cart['bread']} breads for "
                          f"{bread_cost} dollars")

                    print(f"{customer_cart['butter']} butters for "
                          f"{butter_cost} dollars")

                    total_customer_cost = milk_cost + bread_cost + butter_cost

                    print(f"Total cost is {total_customer_cost} dollars")
                    print("See you again!\n")
                    print(info_after_shopping(preferable_shop[0]))
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make purchase in any shop")
