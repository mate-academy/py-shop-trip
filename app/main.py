import json

from pathlib import Path
from typing import List, Dict, Union

from app.car import Car
from app.customer import Customers
from app.shop import Shop


def creating_classes() -> Dict[
    str,
    Union[List[Shop], List[Car], List[Customers], float]
]:

    path = Path("app/config.json")
    with open(path, "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    shops_data = config_data["shops"]
    customers_data = config_data["customers"]

    shops = [
        (Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        ))
        for shop_data in shops_data
    ]

    cars = [Car(
        brand=customer_data["car"]["brand"],
        fuel_consumption=customer_data["car"]["fuel_consumption"]
    )
        for customer_data in customers_data]

    customers = [
        Customers(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        for customer_data, car in zip(customers_data, cars)
    ]

    result = {
        "shops": shops,
        "cars": cars,
        "customers": customers,
        "fuel_price": fuel_price
    }
    return result


def shop_trip() -> None:

    classes = creating_classes()
    best_choice = {}

    for customer in classes["customers"]:
        customer.customer_money()
        for shop in classes["shops"]:

            total_trip_cost = customer.trip_cost(
                shop,
                customer.car,
                classes["fuel_price"]
            )
            milk_cost = customer.product_coast(shop)[0]
            bread_cost = customer.product_coast(shop)[1]
            butter_cost = customer.product_coast(shop)[2]
            total_cost = round(
                total_trip_cost
                + sum(customer.product_coast(shop)),
                2
            )

            best_choice[total_cost] = [
                shop,
                milk_cost,
                bread_cost,
                butter_cost
            ]

            rest_money = customer.money - min(best_choice)
            best_choice[total_cost].append(rest_money)

            customer.customer_best_choice(shop, total_cost)

        milks_coast = best_choice[min(best_choice)][1]
        breads_coast = best_choice[min(best_choice)][2]
        butters = best_choice[min(best_choice)][3]
        buy_coast = milks_coast + breads_coast + butters
        best_shop = best_choice[min(best_choice)][0]

        if best_choice[min(best_choice)][4] < 0:
            customer.not_enough_money()
        else:
            customer.customer_rides_to_shop(best_shop)

            customer.customer_check(
                milks_coast,
                breads_coast,
                butters,
                buy_coast
            )

            customer.customer_rides_home(min(best_choice))
