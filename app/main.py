import datetime
import json
import math

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Customer:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.products_dict_needed = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car_consumption = data["car"]["fuel_consumption"]


class Shop:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.location = data["location"]
        self.products_dict = data["products"]
        self.trip_costs = None


def parse_json_file():
    with open(BASE_DIR / "config.json", "r") as f:
        data_dict = json.load(f)

    return data_dict


def cost_of_the_trip(
        fuel_price: int,
        fuel_consumption: int,
        customer_location: list,
        shop_location: list,
        customer_products_needed: dict,
        shop_products_prices: dict,
):
    distance = math.dist(customer_location, shop_location) * 2
    fuel_cost = (distance * fuel_consumption) / 100 * fuel_price

    trip_cost_data_dict = {"products": {}}
    total_product_cost = 0

    for product, amount in customer_products_needed.items():
        product_cost = amount * shop_products_prices[product]
        trip_cost_data_dict["products"][product] = (amount, product_cost)
        total_product_cost += product_cost

    trip_cost_data_dict["total_product_cost"] = total_product_cost
    trip_cost_data_dict["the_whole_cost"] = total_product_cost + fuel_cost

    return trip_cost_data_dict


def shop_trip():
    data_dict = parse_json_file()
    fuel_price = data_dict["FUEL_PRICE"]

    customers_list = [
        Customer(customer_data)
        for customer_data in data_dict["customers"]
    ]
    shops_list = [
        Shop(shop_data)
        for shop_data in data_dict["shops"]
    ]

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        shop_and_its_whole_cost = {}
        for shop in shops_list:
            shop.trip_costs = cost_of_the_trip(
                fuel_price,
                customer.car_consumption,
                customer.location,
                shop.location,
                customer.products_dict_needed,
                shop.products_dict
            )

            shop_and_its_whole_cost[shop] = shop.trip_costs["the_whole_cost"]
            cost_of_the_trip_to_each_shop = round(
                shop.trip_costs['the_whole_cost'], 2
            )
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {cost_of_the_trip_to_each_shop}")

        best_price = customer.money
        chosen_shop = None
        for shop, cost in shop_and_its_whole_cost.items():
            if cost <= best_price:
                best_price = cost
                chosen_shop = shop

        if chosen_shop is not None:
            print(f"{customer.name} rides to {chosen_shop.name}\n")

            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            has_bought = chosen_shop.trip_costs["products"].items()
            for product, (amount, cost) in has_bought:
                print(f"{amount} {product}s for {cost} dollars")
            products_cost = chosen_shop.trip_costs['total_product_cost']
            print(f"Total cost is {products_cost} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            spent_money = round(chosen_shop.trip_costs["the_whole_cost"], 2)
            the_rest_of_money = customer.money - spent_money
            print(f"{customer.name} now has {the_rest_of_money} dollars\n")

        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make purchase in any shop")
