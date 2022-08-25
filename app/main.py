import json
from typing import List

from app.customer import Customer
from app.shop import Shop
from app.trip import Trip


def go_shopping(
        customer: Customer,
        shops: List[Shop],
        fuel_price: float) -> str:
    trips = [Trip(customer, shop, fuel_price) for shop in shops]

    print(f"{customer.name} has {customer.money} dollars")

    for trip in trips:
        print(f"{customer.name}'s trip to the {trip.shop.name} "
              f"costs {trip.cost_of_trip}")

    trip = min(trips, key=lambda x: x.cost_of_trip)

    if customer.money >= trip.cost_of_trip:
        print(f"{customer.name} rides to {trip.shop.name}")
        print("")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for key, value in trip.cash_bill.items():
            print(f"{key} for {value} dollars")

        print(f"Total cost is {trip.cost_of_cart} dollars")
        print("See you again!")
        print("")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {trip.cash_rest} dollars")
    else:
        print(f"{customer.name} doesn't have enough money "
              "to make purchase in any shop")


def shop_trip():
    with open("app/config.json", "r") as f:
        source_data = json.load(f)

    fuel_price = source_data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in source_data["customers"]]
    shops = [Shop(shop) for shop in source_data["shops"]]

    for customer in customers:
        if customer != customers[0]:
            print("")

        go_shopping(customer, shops, fuel_price)
