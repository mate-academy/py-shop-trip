import math
import json
import datetime
from typing import List


def calculate_distance(coordinates1: List[int],
                       coordinates2: List[int]) -> float:
    x1, y1 = coordinates1
    x2, y2 = coordinates2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def calculate_distance_price(fuel_price: float,
                             fuel_consumption: float,
                             distance: float) -> float:
    fuel_used = (fuel_consumption / 100) * distance
    return fuel_price * fuel_used * 2


def calculate_products_price(product_cart: dict,
                             shop_products: dict) -> int:
    price = 0
    for item in product_cart:
        number_of_products = product_cart[item]
        price_of_products = shop_products[item]
        final_price = number_of_products * price_of_products
        price += final_price
    return price


def printing_check(product_cart: dict,
                   shop_products: dict,
                   customer_name: str) -> None:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("Date: %d/%m/%Y %H:%M:%S")
    print(formatted_datetime)

    final_price = 0

    print(f"Thanks, {customer_name}, for your purchase!")
    print("You have bought: ")
    for product, quantity in product_cart.items():
        price = quantity * shop_products[product]
        final_price += price
        print(f"{quantity} {product}s for {price} dollars")
    print(f"Total cost is {final_price} dollars")
    print("See you again!\n")


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

    customers = data["customers"]
    shops = data["shops"]
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        customer_name = customer["name"]
        customer_money = customer["money"]
        print(f"{customer_name} has {customer_money} dollars")

        total_price = float("inf")
        preferred_shop = None
        preferred_shop_name = None

        fuel_consumption = customer["car"]["fuel_consumption"]

        for shop in shops:
            name_of_shop = shop["name"]
            # Ride price
            distance = calculate_distance(customer["location"],
                                          shop["location"])

            price_to_ride = calculate_distance_price(fuel_price,
                                                     fuel_consumption,
                                                     distance)
            # Shopping price
            price_of_shopping = calculate_products_price(
                customer["product_cart"],
                shop["products"])

            final_price = round(price_to_ride + price_of_shopping, 2)

            print((f"{customer_name}'s trip to the "
                   f"{name_of_shop} costs {final_price}"))

            if final_price < total_price:
                total_price = final_price
                preferred_shop_name = name_of_shop
                preferred_shop = shop

        if total_price <= customer_money:
            customer["money"] -= total_price
            print(f"{customer_name} rides to {preferred_shop_name}\n")

            printing_check(customer["product_cart"],
                           preferred_shop["products"],
                           customer_name)

            print(f"{customer_name} rides home")
            print(f"{customer_name} now has {customer['money']} dollars\n")

        else:
            print((f"{customer_name} doesn't have enough "
                   f"money to make a purchase in any shop"))


shop_trip()
