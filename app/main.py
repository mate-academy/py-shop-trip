import datetime
import json
from math import dist

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    fuel_price = 0
    customers = []
    shops = []

    with open("app/config.json", "r") as config:
        initialization_data = json.load(config)
        fuel_price = initialization_data["FUEL_PRICE"]
        for customer in initialization_data["customers"]:
            customer["car"] = Car(**customer["car"])
            customers.append(Customer(**customer))

        for shop in initialization_data["shops"]:
            shops.append(Shop(**shop))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        minimal_cost_trip = None
        for shop in shops:
            distance = dist(customer.location, shop.location) * 2
            cost_of_trip = round(
                (distance
                 * (customer.car.fuel_consumption / 100) * fuel_price), 2)

            cost_of_products = 0
            for product, quantity in customer.product_cart.items():
                cost_of_products += quantity * shop.products[product]

            total_cost = round(cost_of_trip + cost_of_products, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

            if minimal_cost_trip is None or total_cost < minimal_cost_trip[1]:
                minimal_cost_trip = [shop, total_cost]

        if not customer.money >= minimal_cost_trip[1]:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            customer.ride_to(minimal_cost_trip[0])
            date = datetime.datetime.now()
            minimal_cost_trip[0].print_receipt(customer, date)
            print()
            customer.ride_home(minimal_cost_trip[1])
            print()
