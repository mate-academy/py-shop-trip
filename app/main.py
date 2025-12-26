import json
import math

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = [Shop(**shop) for shop in data["shops"]]
    for people in customers:
        customer = Customer(
            people["name"],
            people["product_cart"],
            people["location"],
            people["money"],
            Car(**people["car"])
        )
        print(f"{customer.name} has {customer.money} dollars")
        prices = {}
        for shop in shops:
            cost = round(shop.trip_cost(
                math.dist(customer.location,shop.location),
                fuel_price,
                customer
            ), 2)
            prices[cost] = shop
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        cost_of_ride = min([price for price in prices])
        if cost_of_ride <= customer.money:
            print(f"{customer.name} rides to {prices[cost_of_ride].name}\n")
            prices[cost_of_ride].print_receipt(customer)
            print(f"{customer.name} rides home")
            customer.money -= cost_of_ride
            print(f"{customer.name} now has {customer.money} dollars\n")
            continue
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")
