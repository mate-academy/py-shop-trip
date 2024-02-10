import json
import os
from math import isclose

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    with open(os.path.join("app", "config.json")) as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]

    customers = []
    for customer_data in config_data["customers"]:
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            car,
        )
        customers.append(customer)

    shops = []
    for shop_data in config_data["shops"]:
        shop = Shop(shop_data["name"], shop_data["location"], shop_data["products"])
        shops.append(shop)

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")
        min_trip_cost = float('inf')
        selected_shop = None

        for shop in shops:
            distance_to_shop = Customer.calculate_distance(customer.location, shop.location)
            fuel_cost_to_shop = (distance_to_shop / 100) * customer.car.fuel_consumption * fuel_price
            product_cost = sum(customer.product_cart[item] * shop.products[item] for item in customer.product_cart)
            fuel_cost_to_home = (distance_to_shop / 100) * customer.car.fuel_consumption * fuel_price

            total_trip_cost = fuel_cost_to_shop + product_cost + fuel_cost_to_home
            print(f"{customer.name}'s trip to the {shop.name} costs {round(total_trip_cost, 2)}")


            if isclose(total_trip_cost, min_trip_cost) and total_trip_cost <= customer.money:
                min_trip_cost = total_trip_cost
                selected_shop = shop

        if selected_shop:
            print(f"{customer.name} rides to {selected_shop.name}")
            customer.purchase_receipt(selected_shop.name, selected_shop.products)
            print(f"{customer.name} rides home")
            customer.money -= min_trip_cost
            print(f"{customer.name} now has {round(customer.money, 2)} dollars")

        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
