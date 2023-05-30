import json

import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

        fuel_price = data["FUEL_PRICE"]
        customers = [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            )
            for customer in data["customers"]
        ]
        shops = [
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            for shop in data["shops"]
        ]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            trips_cost = {}

            for shop in shops:
                fuel_cost = (
                    customer.car.get("fuel_consumption") / 100
                    * customer.calculate_distance(shop)
                    * fuel_price
                )
                trip_cost = (
                    fuel_cost * 2 + customer.calculate_products_cost(shop)
                )
                trips_cost[trip_cost] = shop
                print(
                    f"{customer.name}'s trip to the {shop.name} "
                    f"costs {round(trip_cost, 2)}"
                )
            cheapest_trip = min(trips_cost)
            optimal_shop = trips_cost[cheapest_trip]

            if customer.money < cheapest_trip:
                print(
                    f"{customer.name} doesn't have enough money "
                    f"to make a purchase in any shop"
                )
            else:
                print(f"{customer.name} rides to {optimal_shop.name}\n")
                print(
                    datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S")
                )
                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought: ")
                total_cost = 0

                for product, quantity in customer.product_cart.items():
                    product_price = quantity * optimal_shop.products[product]
                    total_cost += product_price
                    print(f"{quantity} {product}s for {product_price} dollars")

                print(f"Total cost is {total_cost} dollars")
                print("See you again!\n")
                print(f"{customer.name} rides home")
                print(
                    f"{customer.name} now has "
                    f"{round(customer.money - cheapest_trip, 2)} dollars\n"
                )
