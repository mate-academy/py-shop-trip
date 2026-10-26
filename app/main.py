import json
from pathlib import Path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).with_name("config.json")
    with config_path.open("r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    shops = [Shop(**shop_data) for shop_data in config["shops"]]
    for customer_data in config["customers"]:
        customer = Customer(**customer_data)
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = []
        for shop in shops:
            cost = customer.trip_cost(shop, config["FUEL_PRICE"])
            trip_costs.append((shop, cost))
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{cost:.2f}"
            )

        affordable = [
            (shop, cost)
            for shop, cost in trip_costs
            if cost <= customer.money
        ]
        if not affordable:
            print(
                f"{customer.name} doesn't have enough money to make a "
                "purchase in any shop"
            )
            continue

        shop, _ = min(affordable, key=lambda option: option[1])
        customer.go_to(shop, config["FUEL_PRICE"])
        print(f"{customer.name} rides to {shop.name}")
        print()
        shop.sell_products(customer)
        print()
        customer.go_home()
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()
