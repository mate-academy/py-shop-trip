from app.car import Car

from app.shop import Shop

from app.customer import Customer


import json


def shop_trip() -> None:
    with open("app/config.json", "r") as json_file:
        data = json.load(json_file)
    fuel_price = data["FUEL_PRICE"]
    list_of_shops = []
    for value in data["shops"]:
        list_of_shops.append(
            Shop(
                value["name"],
                value["location"],
                value["products"]
            )
        )
    list_of_customers = []
    for value in data["customers"]:
        list_of_customers.append(
            Customer(
                value["name"],
                value["product_cart"],
                value["location"],
                value["money"],
                Car(
                    value["car"]["brand"],
                    value["car"]["fuel_consumption"]
                )
            )
        )
    for cust in list_of_customers:
        print(f"{cust.name} has {cust.money} dollars")
        res_cust_calculate = cust.calculates_the_price(list_of_shops,
                                                       fuel_price)
        if res_cust_calculate:
            print()
            for value in list_of_shops:
                if res_cust_calculate[1] == value.name:
                    value.take_a_check(res_cust_calculate)
            print()
            print(f"{cust.name} rides home")
            print(f"{cust.name} now has {round(cust.money, 2)} dollars")
            print()
