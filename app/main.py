import json
from decimal import Decimal

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)
    fuel_price = config["FUEL_PRICE"]
    list_of_shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]
    list_of_customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            Decimal(customer["money"]),
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"]),
        )
        for customer in config["customers"]
    ]
    for customer in list_of_customers:
        money_str = str(round(customer.money, 2)).rstrip("0").rstrip(".")
        print(f"{customer.name} has {money_str} dollars")
        shop_price_dict = {}
        for shop in list_of_shops:
            try:
                shop_price_dict[shop] = customer.calculate_shop_trip(
                    shop, fuel_price
                )
            except KeyError:
                print(f"{shop.name} does not have {customer.name}'s "
                      f"required product. {shop.name} is "
                      f"excluded from calculation.")
        cheapest_shop = min(shop_price_dict, key=shop_price_dict.get)
        for key, value in shop_price_dict.items():
            print(
                f"{customer.name}'s trip to "
                f"the {key.name} costs {round(value, 2)}"
            )
        if customer.money < shop_price_dict[cheapest_shop]:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue
        print(f"{customer.name} rides to {cheapest_shop.name}")
        customer.ride(cheapest_shop, shop_price_dict[cheapest_shop])
