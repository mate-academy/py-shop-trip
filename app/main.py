import json
import os
from decimal import Decimal

from app.car import Car
from app.customer import Customer
from app.shop import Shop

current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.json")

with open(config_file_path, "r") as config_file:
    information = json.load(config_file)

FUEL_PRICE = Decimal(information["FUEL_PRICE"])

customers_inform = information["customers"]
all_customers = []
for customer_inform in customers_inform:
    one_customer = Customer(
        customer_inform["name"],
        customer_inform["product_cart"],
        customer_inform["location"],
        Decimal(customer_inform["money"]),
        Car(
            customer_inform["car"]["brand"],
            Decimal(customer_inform["car"]["fuel_consumption"]),
        ),
    )
    all_customers.append(one_customer)

shops_inform = information["shops"]
all_shops = []
for shop_inform in shops_inform:
    one_shop = Shop(
        shop_inform["name"], shop_inform["location"], shop_inform["products"]
    )
    all_shops.append(one_shop)


def shop_trip() -> None:
    for customer in all_customers:
        print(f"{customer.name} has {customer.money} dollars")

        all_shop_cost = []

        for shop in all_shops:
            some_cost = customer.cost_product(
                shop.products,
                FUEL_PRICE,
                shop.location
            )
            all_shop_cost.append([shop, some_cost])
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {some_cost}")

        min_cost = all_shop_cost[0][1]
        cheapest_shop = all_shop_cost[0][0]
        for i in range(len(all_shop_cost)):
            if all_shop_cost[i][1] < min_cost:
                min_cost = all_shop_cost[i][1]
                cheapest_shop = all_shop_cost[i][0]

        if min_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            cheapest_shop.make_recipe(customer.product_cart)
            print(f"{customer.name} rides home")
            customer.update_person_money(min_cost)
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


shop_trip()
