import datetime
import json
import os

from typing import List

from app.auxilaries.car import Car
from app.auxilaries.customer import Customer
from app.auxilaries.shop import Shop


def parse_data_from_json() -> list:
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.abspath(
        os.path.join(current_directory, os.pardir)
    )
    config_file_path = os.path.join(parent_directory, "config.json")
    with open(config_file_path, "r") as json_file:
        json_data = json.load(json_file)

    json_fuel_price = json_data["FUEL_PRICE"]
    json_customers = json_data["customers"]
    json_shops = json_data["shops"]

    return [json_fuel_price, json_customers, json_shops]


def create_customer_classes(json_customers: list) -> List[Customer]:
    customer_list = []
    for line in json_customers:
        car = Car(
            line["car"]["brand"],
            line["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=line["name"],
            product_cart=line["product_cart"],
            location=line["location"],
            money=line["money"],
            car=car
        )
        customer_list.append(customer)

    return customer_list


def create_shops_classes(json_shops: list) -> List[Shop]:
    shop_list = []
    for line in json_shops:
        shop = Shop(
            name=line["name"],
            location=line["location"],
            products=line["products"]
        )
        shop_list.append(shop)

    return shop_list


def define_destination_shop(
        customer: Customer,
        shops: List[Shop]
) -> Shop:
    for shop in shops:
        shop.total_cost = round(
            (customer.get_fuel_cost(customer.car, shop) * 2
             + customer.calculate_product_cost(shop)), 2
        )
        print(f"{customer.name}'s trip to the {shop.name}"
              f" costs {shop.total_cost}")
    best_cost_shop = min(shops, key=lambda x: x.total_cost)
    if customer.money > best_cost_shop.total_cost:
        print(f"{customer.name} rides to {best_cost_shop.name}")
        return best_cost_shop
    print(f"{customer.name} doesn't have enough "
          f"money to make a purchase in any shop")


def format_money(value: str | int) -> str:
    if str(value) != str(int(value)):
        value = str(value).rstrip("0").rstrip(".")
        return value
    return value


def print_receipt(
        customer_name: str,
        printed_list: list,
        receipt_total: str
) -> None:
    current_time = datetime.datetime.now()
    check_date = current_time.strftime("%d/%m/%Y %H:%M:%S")
    print(f"\n"
          f"Date: {check_date}\n"
          f"Thanks, {customer_name}, for your purchase!\n"
          f"You have bought: ")
    for item in printed_list:
        print(item)
    print(f"Total cost is {receipt_total} dollars\n"
          f"See you again!\n")
