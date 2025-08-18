import json
import os

from app.customer import Customer
from app.shop import Shop

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "config.json")


def shop_trip() -> None:
    with open(path) as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(data, fuel_price) for data in config["customers"]]
    shops = [Shop(data) for data in config["shops"]]

    for customer in customers:
        money_str = f"{customer.money:.2f}".rstrip('0').rstrip('.')

        print(f"{customer.name} has {money_str} dollars")

        affordable_shops = []
        for shop in shops:
            can_afford, cost = customer.can_afford_trip(shop)
            cost_str = f"{cost:.2f}".rstrip('0').rstrip('.')
            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost_str}"
            )
            if can_afford:
                affordable_shops.append((shop, cost))
        if affordable_shops:
            best_shop, _ = min(affordable_shops, key=lambda s: s[1])
            customer.buy_from(best_shop)
        else:
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )


shop_trip()
