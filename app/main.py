import json
import os

from app.customer import Customer
from app.shop import Shop
from decimal import Decimal
from app.car import Car


def shop_trip() -> None:
    def reader_json() -> dict:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as file_json:
            return json.load(file_json)

    data = reader_json()

    list_customer = []
    for custom in data["customers"]:
        car = Car(**custom["car"])
        customer = Customer(
            name=custom["name"],
            product_cart=custom["product_cart"],
            location=custom["location"],
            money=Decimal(custom["money"]),
            car=car
        )
        list_customer.append(customer)

    list_shop = []
    for shop in data["shops"]:
        list_shop.append(Shop(**shop))

    for custom in list_customer:
        print(f"{custom.name} has {custom.money} dollars")
        all_cost_list = []

        for shop in list_shop:
            cost = custom.will_cost(shop)
            shopping = sum(cost)
            cost_to_shop = custom.car.distance_to_shop(custom, data, shop)

            total_cost_trip = shopping + cost_to_shop
            print(
                f"{custom.name}'s trip to the "
                f"{shop.name} costs {total_cost_trip}"
            )
            all_cost_list.append(total_cost_trip)

        min_value = min(all_cost_list)
        if custom.money < min_value:
            print(
                f"{custom.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        else:
            min_cost_shop = all_cost_list.index(min_value)
            select_shop = list_shop[min_cost_shop]
            print(f"{custom.name} rides to {str(select_shop)}\n")
            custom.create_check(select_shop)

            custom.custom_at_home(min_value)
