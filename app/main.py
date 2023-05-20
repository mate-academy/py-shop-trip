from __future__ import annotations
import json

from app.customer import Customer
from app.shop import Shop
from app.car import trip_cost


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        content = json.load(config)

    fuel_price = content["FUEL_PRICE"]
    for customer in content["customers"]:
        buyer = Customer(customer["name"],
                         customer["product_cart"],
                         customer["location"],
                         customer["money"],
                         customer["car"],
                         fuel_price
                         )
        print(f"{buyer.name} has {buyer.money} dollars")
        for shop in content["shops"]:
            store = Shop(shop["name"],
                         shop["location"],
                         shop["products"])
            cost = buyer.total_cost_to_shop(store)
            print(f"{buyer.name}'s trip to the {store.name} costs {cost}")
        best_shop = buyer.the_best_shop()

        if best_shop:
            best_shop = Shop(best_shop["name"],
                             best_shop["location"],
                             best_shop["products"])
            buyer.money -= trip_cost(buyer, best_shop)
            best_shop.buying_product(buyer)
            print(f"{buyer.name} rides home\n"
                  f"{buyer.name} now has {buyer.money} dollars\n")


shop_trip()
