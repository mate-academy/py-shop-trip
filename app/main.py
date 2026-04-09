import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car
from pathlib import Path


def shop_trip() -> None:
    current_dir = Path(__file__).parent
    config_path = current_dir.parent / "config.json"
    with open(config_path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [
        Shop(s["name"], s["location"], s["products"])
        for s in data["shops"]
    ]

    customers = []
    for customer in data["customers"]:
        customer_car = Car(customer["car"]["brand"],
                           customer["car"]["fuel_consumption"])
        new_customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer_car
        )
        customers.append(new_customer)

    for index, customer in enumerate(customers):

        if index > 0:
            print()

        print(f"{customer.name} has {round(customer.money, 2)} dollars")
        home_location = list(customer.location)

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(cost, 2)}")

            if cost < min_trip_cost:
                min_trip_cost = cost
                cheapest_shop = shop

        if customer.money >= min_trip_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.money -= min_trip_cost
            customer.drive_to(cheapest_shop.location)
            customer.buy_products(cheapest_shop)
            print()
            print(f"{customer.name} rides home")
            customer.drive_to(home_location)
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
