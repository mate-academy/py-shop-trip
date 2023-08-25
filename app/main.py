import json
import datetime
import os
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    current_directory = os.path.dirname(__file__)
    json_file_path = os.path.join(current_directory, "config.json")
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    fuel_price = data["FUEL_PRICE"]
    customer_list = []
    shop_dict = {}
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
        shop_dict[shop["name"]] = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        total_cost_dict = {}
        for shop in shop_dict.values():
            trip_cost = customer.calculate_trip_cost(
                shop.location,
                fuel_price
            )
            products_cost = shop.customer_total_price(
                customer.products
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
        cheapest_shop = shop_dict[cheapest_shop_name]
        cheapest_total = cheapest_shop.customer_total_price(
            customer.products
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
