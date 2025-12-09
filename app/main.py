from __future__ import annotations

import datetime
import json
import os
from decimal import Decimal

from app.customer import Customer
from app.shop import Shop
from app.shopping import Shopping


def shop_trip() -> None:
    apostrophe = "\'"
    path_to_json = create_path_to_json(os.getcwd())
    path_to_json = os.path.join(path_to_json, "config.json")
    with open(path_to_json, "r") as file:
        all_info = json.load(file)

    fuel_price = extract_fuel_price(all_info)
    customers = extract_customers(all_info)
    shops = extract_shops(all_info)

    cheapest_shopping_by_customer = dict()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            print(f"{customer.name}{apostrophe}s trip to the "
                  f"{shop.name} costs "
                  f"{Shopping(customer, shop, fuel_price).total_amount}")

        cheapest_shopping_found = cheapest_shopping(customer)
        cheapest_shopping_dict = cheapest_shopping_found.__dict__
        cheapest_shopping_by_customer[customer.name] = cheapest_shopping_dict
        shop_name = cheapest_shopping_dict.get("shop").name

        if customer.money < cheapest_shopping_found.products_cost():
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        print(f"{customer.name} rides to {shop_name}")
        print("")
        shopping_report(cheapest_shopping_found)
        print()


def one_product_cost(one_amount: Decimal) -> int | Decimal:
    result = one_amount
    if abs(one_amount // 1 - one_amount) < 0.000001:
        result = int(one_amount // 1)
    return result


def create_path_to_json(current_path: str) -> str:
    result = current_path

    last_5_symbols = current_path[len(current_path) - 5:]

    if current_path.count("app") == 0 and last_5_symbols != "tests":
        result = os.path.join(result, "app")

    if last_5_symbols == "tests":
        result = current_path[:len(current_path) - 5]
        result = os.path.join(result, "app")
    return result


def cheapest_shopping(customer: Customer) -> Shopping | None:
    one_customer_shoppings = []
    for one_shopping in Shopping.shopping_registry:
        if one_shopping.customer is customer:
            one_customer_shoppings.append(one_shopping)

    if len(one_customer_shoppings) == 0:
        return None
    else:

        current_expences = one_customer_shoppings[0].total_amount
        result = one_customer_shoppings[0]
        for one_shopping in one_customer_shoppings:
            if one_shopping.total_amount < current_expences:
                current_expences = one_shopping.total_amount
                result = one_shopping
    return result


def shopping_report(shopping: Shopping) -> None:
    shopping_dict = shopping.__dict__
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {current_time_str}")
    current_customer = shopping_dict.get("customer")
    print(f"Thanks, {current_customer.name}, for your purchase!")
    print("You have bought:")
    current_product_cart = current_customer.product_cart
    current_shop_products = shopping_dict.get("shop").products
    for one_product, quantity in current_product_cart.items():
        one_product_price = current_shop_products.get(one_product)
        print(f"{quantity} {one_product}s "
              f"for {one_product_cost(one_product_price * quantity)} dollars")
    # print(f"Total cost is {shopping.products_cost()} dollars")
    print(f"Total cost is {shopping.products_cost()} dollars")
    print("See you again!")
    print("")
    print(f"{current_customer.name} rides home")
    money_left = current_customer.money - shopping.total_amount
    print(f"{current_customer.name} now has {money_left} dollars")


def extract_customers(all_info: dict) -> list:
    customers_part = all_info.get("customers")
    result = []
    for one_customer in customers_part:
        result.append(Customer(one_customer["name"],
                               one_customer["product_cart"],
                               one_customer["location"],
                               one_customer["money"],
                               one_customer["car"]))
    return result


def extract_fuel_price(all_info: dict) -> Decimal:
    return all_info.get("FUEL_PRICE")


def extract_shops(all_info: dict) -> list:
    shops_part = all_info.get("shops")
    result = []
    for one_shop in shops_part:
        result.append(Shop(one_shop["name"],
                           one_shop["location"],
                           one_shop["products"]))
    return result


if __name__ == "__main__":
    shop_trip()
