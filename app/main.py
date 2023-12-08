import json
import os
from typing import List
from app.customers import Customer
from app.cars import Car
from app.shops import Shop


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = push_customers_data_to_class(data["customers"])
    shops = push_shops_data_to_class(data["shops"])

    for customer in customers:
        print_customer_trip(customer, shops, fuel_price)


def print_customer_trip(
        customer: Customer,
        shops: List[Shop],
        fuel_price: float
) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    cheapest_shop = (shops[0], float("inf"))
    for shop in shops:
        amount = customer.count_trip_cost(shop, fuel_price)
        if amount < cheapest_shop[1]:
            cheapest_shop = (shop, amount)
        print(f"{customer.name}'s trip to the {shop.name} costs {amount}")
    if customer.money < cheapest_shop[1]:
        print((f"{customer.name} doesn't have enough "
               "money to make a purchase in any shop"))
    else:
        print(f"{customer.name} rides to {cheapest_shop[0].name}\n")
        cheapest_shop[0].print_check(customer)
        print(f"{customer.name} rides home")
        change = customer.money - cheapest_shop[1]
        print(f"{customer.name} now has {change} dollars\n")


def push_customers_data_to_class(people: list) -> list[Customer]:
    customers = []
    for person in people:
        car = Car(person["car"]["brand"], person["car"]["fuel_consumption"])
        customers.append(Customer(
            person["name"],
            person["product_cart"],
            person["location"],
            person["money"],
            car
        ))
    return customers


def push_shops_data_to_class(markets: list) -> list[Shop]:
    shops = []
    for market in markets:
        shops.append(Shop(
            market["name"],
            market["location"],
            market["products"]
        ))
    return shops
