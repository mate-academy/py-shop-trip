import json
import math

from app.car import Car
from app.customer import Customer
from app.shop import Shops


def shop_trip():

    with open("app/config.json", "r") as data_file:
        data = json.load(data_file)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    customer_list = []
    for customer in customers:
        customer_list.append(Customer
                    (customer["name"],
                     customer["product_cart"],
                     customer["location"],
                     customer["money"],
                     Car
                     (customer["car"]["brand"],
                      customer["car"]["fuel_consumption"])))

    shop_list = []
    for shop in shops:
        shop_list.append(Shops(shop["name"],
                               shop["location"],
                               shop["products"]))

    min_cost = float("inf")
    best_shop = None

    for customer in customer_list:

        customer.customer_money()
        for shop in shop_list:

            total_price_road = customer.distance(
                shop.shop_location,
                fuel_price,
                customer.car.fuel_consumption)
            total_cost_product = customer.shopping_time
            all_total_cost = total_price_road + sum(
                price * shop.products[products_name] for products_name, price in customer.products_cart.items())

            print(f"{customer.name}'s trip to the {shop.name} costs {round(all_total_cost, 2)}")

            if all_total_cost < min_cost and all_total_cost <= customer.money:
                min_cost = all_total_cost
                best_shop = shop

        if customer.money < all_total_cost:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")

        if best_shop is not None:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.shopping_time(best_shop)
            customer.money -= min_cost
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
