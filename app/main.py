import json
import os

from app.car import Car
from app.customers import Customer
from app.shops import Shop

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")


def shop_trip() -> None:
    with open(CONFIG_PATH, "r") as file:
        my_json = json.load(file)

        fuel_price = my_json["FUEL_PRICE"]
        customers = [Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"])
        ) for customer in my_json["customers"]]
        shops = [Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in my_json["shops"]]

        for customer in customers:
            prices = {}
            customer_home_location = customer.location
            print(f"{customer.name} has {customer.money} dollars")
            for shop in shops:
                distance_to_shop = shop.distance_to_shop(customer.location)
                road_price = customer.car.road_price(
                    distance_to_shop, fuel_price
                )
                total_price = shop.products_cost(customer.product_cart)
                trip_total_cost = round(road_price + total_price, 2)
                prices[shop] = {
                    "total_costs": trip_total_cost,
                    "road_price": road_price
                }
                print(
                    f"{customer.name}'s trip to the {shop.name} "
                    f"costs {trip_total_cost}"
                )

            cheapest_store = min(
                prices, key=lambda shop: prices[shop]["total_costs"]
            )
            cheapest_store_path = prices[cheapest_store]["road_price"]

            if customer.money < (prices[cheapest_store]["total_costs"]):
                print(
                    f"{customer.name} doesn't have enough money "
                    f"to make a purchase in any shop"
                )
                continue

            print(f"{customer.name} rides to {cheapest_store.name}\n")

            customer.location = cheapest_store.location

            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            costs_of_purchased_products = 0
            for product, cost in customer.product_cart.items():
                total = float(cheapest_store.products[product] * cost)
                print(
                    f"{cost} {product}s for "
                    f"{int(total) if total.is_integer() else total} dollars"
                )
                costs_of_purchased_products += total

            print(f"Total cost is {costs_of_purchased_products} dollars")

            customer.spend(costs_of_purchased_products)
            customer.spend(cheapest_store_path)

            print("See you again!\n")
            print(f"{customer.name} rides home")

            customer.location = customer_home_location

            print(f"{customer.name} now has {customer.money} dollars\n")
