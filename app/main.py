import datetime
import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = (
        Path(__file__).resolve().parent
        / "config.json"
    )

    with open(config_path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = []

    for shop_data in data["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )

        shops.append(shop)

    customers = []

    for customer_data in data["customers"]:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=(
                customer_data["car"]["fuel_consumption"]
            )
        )

        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )

        customers.append(customer)

    for customer in customers:
        print(
            f"{customer.name} has "
            f"{customer.money:g} dollars"
        )

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(
                shop=shop,
                fuel_price=fuel_price
            )

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {trip_cost:.2f}"
            )

            if (
                cheapest_cost is None
                or trip_cost < cheapest_cost
            ):
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if (
            cheapest_shop is None
            or cheapest_cost is None
            or not customer.has_enough_money(
                cheapest_cost
            )
        ):
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue

        print(
            f"{customer.name} rides to "
            f"{cheapest_shop.name}"
        )
        print()

        customer.ride_to(cheapest_shop.location)

        cheapest_shop.print_receipt(
            customer_name=customer.name,
            product_cart=customer.product_cart,
            purchase_time=datetime.datetime.now()
        )

        print()
        print(f"{customer.name} rides home")

        customer.ride_to(customer.home_location)
        customer.pay(cheapest_cost)

        print(
            f"{customer.name} now has "
            f"{customer.money:.2f} dollars"
        )
        print()
