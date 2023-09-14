import os
import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


directory = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(directory, "config.json")


def shop_trip() -> None:
    with open(config_path) as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]
    customers_info = data["customers"]
    shops_info = data["shops"]

    cars = [
        Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        for customer in customers_info
    ]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car,
        )
        for customer, car in zip(customers_info, cars)
    ]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in shops_info
    ]

    for customer in customers:
        lowest_amount = float("inf")
        cheapest_shop = None

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            if trip_cost < lowest_amount and trip_cost <= customer.money:
                lowest_amount = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.money -= lowest_amount
            print(f"{customer.name} rides to {cheapest_shop.name}")
            cheapest_shop.print_receipt(customer)
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
