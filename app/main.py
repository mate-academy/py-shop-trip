import datetime

import json
import math

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    fuel_price, customer_list, shop_list = initialize_json()
    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}
        product_cost = 0
        for shop in shop_list:
            product_cost = 0
            first_point = (shop.location[0] - customer.location[0])**2
            second_point = (shop.location[1] - customer.location[1])**2
            destination = math.sqrt(first_point + second_point)
            fuel_consumption = customer.car.fuel_consumption
            fuel_cost = (destination / 100 * fuel_consumption * fuel_price * 2)

            for product in shop.products_provides:
                shop_product = shop.products_provides[product]
                customer_product = customer.products_to_buy[product]
                product_cost += (shop_product * customer_product)

            trip_cost = round(product_cost + fuel_cost, 2)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_cost}")
            trip_costs[trip_cost] = shop

        cheapest_trip = min(trip_costs.keys())
        shop_to_go = trip_costs[cheapest_trip]
        if customer.money > cheapest_trip:
            print(f"{customer.name} rides to {shop_to_go.name}\n")
            current_date = datetime.datetime.now()
            print("Date: " + str(current_date.strftime("%d/%m/%Y %H:%M:%S")))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            product_cost = 0
            for product in shop_to_go.products_provides:
                shop_product = shop_to_go.products_provides[product]
                customer_product = customer.products_to_buy[product]
                product_cost += (shop_product * customer_product)
                print(f"{customer.products_to_buy[product]} {product}s for "
                      f"{(customer_product * shop_product):g} dollars")

            print(f"Total cost is {product_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {customer.money - cheapest_trip} dollars\n")

        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


def initialize_json() -> tuple:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customer_list = []
    shop_list = []
    for customer in config["customers"]:
        customer_list.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            ),
        ))

    for shop in config["shops"]:
        shop_list.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        ))
    return fuel_price, customer_list, shop_list
