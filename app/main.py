import json
from pathlib import Path

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).resolve().parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"],
        )
        for shop_data in config["shops"]
    ]

    for customer_data in config["customers"]:
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(**customer_data["car"]),
        )

        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            cost = shop.trip_cost(customer, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {Shop._format_number(cost)}"
            )

            if cheapest_cost is None or cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_shop = shop

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue
        print(f"{customer.name} rides to {cheapest_shop.name}")
        print()

        cheapest_shop.sell(customer)

        print(f"{customer.name} rides home")
        customer.money -= cheapest_cost
        print(f"{customer.name} now has "
              f"{Shop._format_number(customer.money)} dollars")
        print()
