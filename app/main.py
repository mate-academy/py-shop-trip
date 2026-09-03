import json
import datetime
import math

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    with open("app/config.json", 'r') as f:
        config = json.load(f)
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]
    for customer in customers:
        customer_ = Customer(customer)
        print(f"{customer_.name} has {customer_.money} dollars")
        car_ = Car(customer["car"])
        min_shop_name = None
        min_shop = None
        min_total_cost = None
        min_products_cost = None
        for shop in shops:
            shop_ = Shop(shop)
            distance = shop_.calculate_distance(customer_.get_location())
            way_cost = car_.calculate_fuel_price(fuel_price, distance)
            product_cart = customer_.get_product_cart()
            products_cost = shop_.calculate_products_cost(product_cart)
            sum_cost = products_cost[3]
            total_cost = way_cost + sum_cost
            if min_total_cost is None:
                min_total_cost = total_cost
                min_shop_name = shop_.name
                min_products_cost = products_cost
            if min_total_cost > total_cost:
                min_total_cost = total_cost
                min_shop_name = shop_.name
                min_products_cost = products_cost
            print(f"{customer_.name}'s trip to the {shop_.name} costs {total_cost}")

        if customer_.can_afford(min_total_cost):
            print(f"{customer_.name} rides to {min_shop_name}")
            print()
        else:
            print(f"{customer_.name} doesn't have enough money to make a purchase in any shop")
            continue
        res = round(customer_.money - min_total_cost, 2)
        print(f"Date: {date}")
        print(f"Thanks, {customer_.name}, for your purchase!\n"
              f"You have bought:\n"
              f"{customer_.product_cart['milk']} milks for {min_products_cost[0]} dollars\n"
              f"{customer_.product_cart['bread']} breads for {int(min_products_cost[1])} dollars\n"
              f"{customer_.product_cart['butter']} butters for {min_products_cost[2]} dollars\n"
              f"Total cost is {min_products_cost[3]} dollars\n"
              f"See you again!\n")
        print(f"{customer_.name} rides home\n"
              f"{customer_.name} now has {res} dollars")
