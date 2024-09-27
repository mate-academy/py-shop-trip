import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json") as config:
        data = json.load(config)
    all_customers = [Customer(customer) for customer in data["customers"]]
    all_shops = [Shop(shop) for shop in data["shops"]]
    all_trips = {}
    for customer in all_customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in all_shops:
            all_trips[shop] = customer.trip_cost(shop)
        cheapest_shop = [
            key for key, value in all_trips.items()
            if value == min(all_trips.values())
        ][0]
        if customer.money < min(all_trips.values()):
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            continue
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        customer.purchase(cheapest_shop)


shop_trip()
