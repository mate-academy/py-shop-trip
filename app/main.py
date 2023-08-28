import os
import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop

script_directory = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_directory, "config.json")


def shop_trip() -> None:
    with open(config_path) as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    cars = [
        Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        for customer in customers_data
    ]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car,
        )
        for customer, car in zip(customers_data, cars)
    ]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in shops_data
    ]

    for customer in customers:
        cheapest_cost = float("inf")
        chosen_shop = None

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            if trip_cost < cheapest_cost and trip_cost <= customer.money:
                cheapest_cost = trip_cost
                chosen_shop = shop

        if chosen_shop:
            customer.money -= cheapest_cost
            print(f"{customer.name} rides to {chosen_shop.name}")
            chosen_shop.print_receipt(customer)
            print(f"\n{customer.name} rides home")
            remaining_money = round(customer.money, 2)
            print(f"{customer.name} now has {remaining_money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
