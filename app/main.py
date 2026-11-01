import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = []

    for customer_data in config["customers"]:
        car = Car(**customer_data["car"])
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            car=car,
            money=customer_data["money"],
        )
        customers.append(customer)

    shops = [Shop(**shop_data) for shop_data in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {round(customer.money, 2)} dollars")

        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(trip_cost, 2)}"
            )

            if trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop is None or customer.money < cheapest_cost:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")
        customer.ride(cheapest_shop.location, fuel_price)
        print()

        customer.money -= cheapest_shop.calculate_cost(customer.product_cart)
        cheapest_shop.print_receipt(customer.name, customer.product_cart)
        print()

        print(f"{customer.name} rides home")
        customer.ride(customer.home_location, fuel_price)
        print(
            f"{customer.name} now has " f"{round(customer.money, 2)} dollars"
        )
        print()
