import json
import math
import datetime
import os
from app.car import Car
from app.shop import Shop
from app.customer import Customer
from decimal import Decimal


def calculate_distance(
        point1: list[int],
        point2: list[int]
) -> float:
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def calculate_trip_cost(
        distance: float,
        fuel_consumption: Decimal,
        fuel_cost: Decimal
) -> Decimal:
    total_cost = (distance / 100) * fuel_consumption * fuel_cost
    return Decimal(total_cost)


def find_shop_by_name(shops: list[Shop], name: str) -> Shop:
    for shop in shops:
        if shop.name == name:
            return shop


def calculate_products_total(
        customer_products: dict,
        shops_products: dict
) -> Decimal:
    return Decimal(sum(
        customer_products[item] * shops_products[item]
        for item in customer_products.keys()
    ))


def shop_trip() -> None:
    current_directory = os.path.dirname(__file__)
    json_file_path = os.path.join(current_directory, "config.json")
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    fuel_price = data["FUEL_PRICE"]
    customer_list = []
    shop_list = []
    for customer in data["customers"]:
        customer_list.append(
            Customer(
                name=customer["name"],
                products=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    consumption=customer["car"]["fuel_consumption"]
                )
            )
        )
    for shop in data["shops"]:
        shop_list.append(
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
        )
    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        total_cost_dict = {}
        for shop in shop_list:
            distance = calculate_distance(
                customer.location,
                shop.location
            )
            trip_cost = calculate_trip_cost(
                distance,
                customer.car.consumption,
                fuel_price
            )
            products_cost = calculate_products_total(
                customer.products,
                shop.products
            )
            total_cost = (trip_cost * 2) + products_cost
            total_cost_dict[shop.name] = total_cost
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {round(total_cost, ndigits=2)}")
        cheapest_shop_name = min(
            total_cost_dict,
            key=lambda k: total_cost_dict[k]
        )
        cost = total_cost_dict[cheapest_shop_name]
        if customer.money < cost:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            return
        remain_money = customer.money - cost
        cheapest_shop = find_shop_by_name(shop_list, cheapest_shop_name)
        cheapest_total = calculate_products_total(
            customer.products,
            cheapest_shop.products
        )
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        time_stamp = datetime.datetime.now()
        formatted_time_stamp = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_time_stamp}")
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")
        for item, value in customer.products.items():
            print(f"{value} {item}s for "
                  f"{value * cheapest_shop.products[item]} dollars")
        print(f"Total cost is {round(cheapest_total, ndigits=1)} dollars\n"
              f"See you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{round(remain_money, ndigits=2)} dollars\n")
