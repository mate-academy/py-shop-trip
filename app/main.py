import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {int(customer.money)} dollars")

        trips = []

        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {cost:.2f}"
            )

            trips.append((cost, shop))

        cheapest_cost, cheapest_shop = min(trips, key=lambda x: x[0])

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")

        customer.location = cheapest_shop.location

        cheapest_shop.print_receipt(
            customer.name,
            customer.product_cart
        )

        customer.money -= cheapest_cost

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()
