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

    yield f"{customer.name} has {customer.money} dollars"

    for trip in trips:
        yield f"{customer.name}'s trip to the {trip.shop.name} "\
              f"costs {trip.cost_of_trip}"

    trip = min(trips, key=lambda x: x.cost_of_trip)

    if customer.money >= trip.cost_of_trip:
        yield f"{customer.name} rides to {trip.shop.name}"
        yield ""
        yield "Date: 04/01/2021 12:33:41"
        yield f"Thanks, {customer.name}, for you purchase!"
        yield "You have bought: "

        for key, value in trip.cash_bill.items():
            yield f"{key} for {value} dollars"

        yield f"Total cost is {trip.cost_of_cart} dollars"
        yield "See you again!"
        yield ""
        yield f"{customer.name} rides home"
        yield f"{customer.name} now has {trip.cash_rest} dollars"
    else:
        yield f"{customer.name} doesn't have enough money "\
              "to make purchase in any shop"


def shop_trip():
    with open("app/config.json", "r") as f:
        source_data = json.load(f)

    fuel_price = source_data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in source_data["customers"]]
    shops = [Shop(shop) for shop in source_data["shops"]]

    log = []

    for customer in customers:
        log.append("\n".join(go_shopping(customer, shops, fuel_price)))

    print("\n\n".join(log))
