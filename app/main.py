import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in config_data["customers"]]
    shops = [Shop(shop) for shop in config_data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips = {}

        for shop in shops:
            trips[shop] = customer.calculate_trip_cost(fuel_price, shop)

        lowest_cost = min(trips.values())
        cheapest_shop = next(shop for shop, cost in trips.items()
                             if cost == lowest_cost)

        if lowest_cost <= customer.money:
            customer.go_shopping(cheapest_shop, lowest_cost)
            customer.go_home()
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
