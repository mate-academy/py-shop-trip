import json
import os

from app.customer import create_customers
from app.shop import create_shops
from math import sqrt


def trip_cost() -> list:
    fuel_cost_for_trip = []
    json_path = os.path.join("app", "config.json")
    with open(json_path, "r") as json_file:
        fuel_price = json.load(json_file)["FUEL_PRICE"]

    customer_class = create_customers()
    shop_class = create_shops()

    for customer in customer_class:
        for shop in shop_class:
            distance = sqrt(
                abs((customer.location[0] - shop.location[0]) ** 2
                    + (customer.location[1] - shop.location[1]) ** 2)
            )
            fuel = (customer.car["fuel_consumption"] * distance) / 100
            fuel_cost_for_trip.append(round(fuel * fuel_price * 2, 2))

    purchases = []

    for index, customer in enumerate(customer_class):
        for shop in shop_class:
            total = 0
            for product in customer.product_cart:
                cost = (customer.product_cart[product]
                        * shop.products[product])
                total += cost

            purchases.append(total)

    return [purchases[index] + fuel_cost_for_trip[index]
            for index in range(len(purchases))]
