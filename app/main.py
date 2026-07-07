import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.gas_station import GasStation


def fmt(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return str(round(value, 2))


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    gas_station = GasStation(data["FUEL_PRICE"])
    customers_data = data["customers"]
    shops_data = data["shops"]

    for customer_data in customers_data:
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(
                customer_data["car"]["brand"],
                customer_data["car"]["fuel_consumption"]
            )
        )

        home_location = customer.location

        print(
            f"{customer.name} has {fmt(customer.money)} dollars"
        )

        options = []

        for shop_data in shops_data:
            shop = Shop(**shop_data)

            cost = round(
                customer.trip_cost(shop, gas_station.price),
                2
            )

            options.append((cost, shop))

            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{fmt(cost)}"
            )

        cheapest_cost, cheapest_shop = min(
            options,
            key=lambda x: x[0]
        )

        if not customer.enough_money(cheapest_cost):
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")

        customer.location = cheapest_shop.location

        cheapest_shop.print_receipt(customer)

        customer.pay(cheapest_cost)

        customer.location = home_location

        print(f"\n{customer.name} rides home")
        print(
            f"{customer.name} now has {fmt(customer.money)} dollars"
        )
        print()
