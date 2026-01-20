import os
from typing import Any
from app.utils.io import read_config
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> Any:
    path = os.path.join(os.path.dirname(__file__), "config.json")
    config = read_config(path)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = []
    for customer_data in customers_data:
        car = Car(customer_data["car"]["brand"],
                  customer_data["car"]["fuel_consumption"])
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        customers.append(customer)

    shops = []
    for shop_data in shops_data:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.best_total_cost = float("inf")
        choose_shop = None
        cheapest_total_cost = None

        for shop in shops:
            total_products_cost =\
                shop.total_products_costs(customer.product_cart)
            total_fuel_cost = customer.trip_cost(shop, fuel_price)
            total_cost = total_products_cost + total_fuel_cost
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_cost:.2f}")

            if total_cost < customer.best_total_cost:
                customer.best_total_cost = total_cost
                customer.best_shop = shop.name
                choose_shop = shop
                cheapest_total_cost = total_cost

        cheapest_trip = cheapest_total_cost
        if choose_shop and customer.can_afford(choose_shop, fuel_price):
            home_location = list(customer.location)
            customer.go_to(choose_shop.location)
            choose_shop.print_receipt(customer.name, customer.product_cart)
            customer.go_to(home_location)
            money_after_shopping = round(
                customer.money - cheapest_trip, 2)
            print(f"{customer.name} now has"
                  f" {money_after_shopping} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
