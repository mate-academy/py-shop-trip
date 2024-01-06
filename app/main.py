import json
import os
import datetime
from typing import List

from app.classes.class_customer import Customer
from app.classes.class_shop import Shop


def shop_trip() -> None:
    project_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_directory, "config.json")
    with open(file_path, "r") as config:
        data = json.load(config)
        fuel_price = data["FUEL_PRICE"]
        customers = [
            Customer.crate_customer(customer)
            for customer in data["customers"]
        ]
        shops = [Shop.create_shop(shop) for shop in data["shops"]]
        for customer in customers:
            printing_actions(customer, shops, fuel_price)


def printing_actions(
        customer: Customer,
        shops: List[Shop],
        fuel_price: int | float
) -> None:
    print(
        "{name} has {money} dollars"
        .format(name=customer.name, money=customer.money)
    )
    shop_dict = {shop: customer.shopping(shop, fuel_price) for shop in shops}
    cheapest_shop = min(shop_dict, key=lambda k: shop_dict[k])
    enough_money = any(customer.money >= value for value in shop_dict.values())
    for shop in shops:
        print(
            "{name}'s trip to the "
            "{shop_name} costs {trip_cost}".format(
                name=customer.name,
                shop_name=shop.name,
                trip_cost=shop_dict[shop]
            )
        )
    if not enough_money:
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")
        return
    print("{name} rides to {shop_name}\n".format(
        name=customer.name,
        shop_name=cheapest_shop.name
    ))
    date_time_now = datetime.datetime.now()
    date = date_time_now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {date}\nThanks, {customer.name}, for your purchase!")
    customer.shopping_details(cheapest_shop)
    print(
        "{name} rides home\n"
        "{name} now has {balance} dollars\n"
        .format(
            name=customer.name,
            balance=customer.balance_of_money(cheapest_shop, fuel_price)
        )
    )
