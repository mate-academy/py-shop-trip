import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.utils import distance


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"

    with config_path.open(encoding="utf-8") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in data["shops"]
    ]

    customers: list[Customer] = []

    for cust in data["customers"]:
        car = Car(
            cust["car"]["brand"],
            cust["car"]["fuel_consumption"],
        )
        customers.append(
            Customer(
                cust["name"],
                cust["product_cart"],
                cust["location"],
                cust["money"],
                car,
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        options: list[tuple[float, Shop, float]] = []

        for shop in shops:
            dist = distance(customer.location, shop.location)
            fuel_cost = customer.car.fuel_cost(dist * 2, fuel_price)
            products_cost = shop.products_cost(customer.product_cart)
            total = fuel_cost + products_cost

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {total:.2f}"
            )

            options.append((total, shop, dist))

        affordable = [
            option for option in options
            if customer.money >= option[0]
        ]

        if not affordable:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue

        total, chosen_shop, _ = min(
            affordable,
            key=lambda item: item[0],
        )

        print(f"{customer.name} rides to {chosen_shop.name}")

        customer.location = chosen_shop.location
        chosen_shop.print_receipt(
            customer.name,
            customer.product_cart,
        )

        customer.money -= total

        print(f"{customer.name} rides home")
        customer.location = customer.home
        print(
            f"{customer.name} now has "
            f"{customer.money:.2f} dollars\n"
        )
