import json
from typing import Callable

from app.shop import Shop
from app.customer import Customer


def get_data(info_key: str, creation_func: Callable) -> list:
    with open("app/config.json", "r") as source:
        data = json.load(source)
    return [creation_func(info) for info in data[info_key]]


def shop_trip() -> None:
    customers = get_data("customers", Customer.create_customer)
    shops = get_data("shops", Shop.create_shop)

    for client in customers:
        print(f"{client.name} has {client.money} dollars")

        client_shop_choice = client.choose_shop(shops)
        if client_shop_choice is None:
            print(f"{client.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return
        print(f"{client.name} rides to {client_shop_choice.name}\n")
        client_shop_choice.sell(client)


shop_trip()
