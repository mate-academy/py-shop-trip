import os

import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers: list[Customer] = []
    shops: list[Shop] = []

    cost_go_to_shop: dict[Customer, dict] = {}

    def open_file() -> None:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "config.json")

        with open(file_path) as file:
            information = json.load(file)

        Car.set_fuel_cost(information["FUEL_PRICE"])

        for customer in information["customers"]:
            customers.append(Customer(customer["name"],
                                      customer["product_cart"],
                                      customer["location"],
                                      customer["money"],
                                      Car(customer["car"]["brand"],
                                          customer["car"]["fuel_consumption"])
                                      ))

        for shop in information["shops"]:
            shops.append(Shop(shop["name"],
                              shop["location"],
                              shop["products"]))

    def calculate_cost_ride_to_all_shops() -> None:
        for customer in customers:
            cost_go_to_shop[customer]: dict[Shop:float] = {}
            for shop in shops:
                money_to_spend = 0.0
                money_to_spend += customer.car.calculate_fuel_cost(
                    customer.go_to_location(shop.location))
                money_to_spend += (customer.product_cart["milk"]
                                   * shop.products["milk"])
                money_to_spend += (customer.product_cart["bread"]
                                   * shop.products["bread"])
                money_to_spend += (customer.product_cart["butter"]
                                   * shop.products["butter"])
                money_to_spend += customer.car.calculate_fuel_cost(
                    customer.go_to_home())
                cost_go_to_shop[customer][shop] = round(money_to_spend, 2)

    def calculate_cheaper_shop(customer: Customer) -> Shop:
        min_sum = float("inf")
        for shop in shops:
            if min_sum > cost_go_to_shop[customer][shop]:
                min_sum = cost_go_to_shop[customer][shop]

        for shop in shops:
            if min_sum == cost_go_to_shop[customer][shop]:
                return shop

    open_file()

    calculate_cost_ride_to_all_shops()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost_go_to_shop[customer][shop]}")
        shop_to_go = calculate_cheaper_shop(customer)
        if customer.money < cost_go_to_shop[customer][shop_to_go]:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            continue
        else:
            print(f"{customer.name} rides to {shop_to_go.name}\n")
            customer.money -= customer.car.calculate_fuel_cost(
                customer.go_to_location(shop_to_go.location))
            customer.money -= shop_to_go.receipt(customer)
            print(f"{customer.name} rides home")
            customer.money -= customer.car.calculate_fuel_cost(
                customer.go_to_home())
            customer.money = round(customer.money, 2)
            print(f"{customer.name} now has {customer.money} dollars\n")
