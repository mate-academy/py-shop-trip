import json

from app.shop import Shop
from app.customer import Customer

import datetime


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        fuel_price = data["FUEL_PRICE"]
        customers = [Customer(**customer) for customer in data["customers"]]
        shops = [Shop(**shop) for shop in data["shops"]]
    for customer in customers:
        print(f"{customer.name} has {int(customer.money)} dollars")
        home = customer.location
        result_of_cost_shops = customer.trip_costs(shops, fuel_price)
        for shop in result_of_cost_shops:
            print(
                f"{customer.name}'s trip to the "
                f"{shop['shop_name']} costs {shop['cost']}"
            )
        chosen_shop = min(result_of_cost_shops, key=lambda shop: shop["cost"])
        if chosen_shop["cost"] <= customer.money:
            print(f"{customer.name} rides to {chosen_shop['shop_name']}")
            customer.location = chosen_shop["shop_obj"].location
            print(f"\nDate: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for key, value in customer.product_cart.items():
                price = chosen_shop["products"][key]
                if price == int(price):
                    price = int(price)
                print(
                    f"{value} {key}s for "
                    f"{price} dollars"
                )
            print(f"Total cost is "
                  f"{sum(chosen_shop['products'].values())} dollars")
            print("See you again!")
            print(f"\n{customer.name} rides home")
            customer.location = home
            customer.money -= chosen_shop["cost"]
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
