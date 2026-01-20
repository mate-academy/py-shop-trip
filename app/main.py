import json
from typing import Dict, Any
from customer import Customer
from shop import Shop
from car import Car


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config: Dict[str, Any] = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    customers = []

    for cust in config["customers"]:
        car = Car(cust["car"]["brand"], cust["car"]["fuel_consumption"])
        customers.append(
            Customer(cust["name"],
                     cust["money"],
                     cust["product_cart"],
                     cust["location"],
                     car))

    shops = [Shop(shop["name"],
                  shop["location"],
                  shop["products"]) for shop in config["shops"]]

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")

        best_option = None
        min_total_cost = float("inf")

        for shop in shops:
            distance = customer.distance_to(shop)
            fuel_cost_to_shop = customer.car.trip_cost(distance, fuel_price)
            fuel_cost_home = customer.car.trip_cost(distance, fuel_price)
            total_fuel_cost = fuel_cost_to_shop + fuel_cost_home

            products_cost = shop.calculate_products_cost(customer.product_cart)
            total_trip_cost = products_cost + total_fuel_cost

            print(f"{customer.name}'s trip to "
                  f"{shop.name} costs {total_trip_cost}")

            if total_trip_cost < min_total_cost:
                min_total_cost = total_trip_cost
                best_option = shop

        if best_option and min_total_cost <= customer.money:
            print(f"{customer.name} rides to {best_option.name}")
            customer.location = best_option.location

            best_option.print_receipt(customer.name, customer.product_cart)

            customer.money -= min_total_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} "
                  f"now has {round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
