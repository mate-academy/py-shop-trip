from typing import IO

from customer import Client
from shop import Shop


def create_clients(data: IO) -> dict:
    clients = {}

    for client_data in data["customers"]:
        name = client_data["name"]
        client = Client(
            name=name,
            product_cart=client_data["product_cart"],
            location=client_data["location"],
            money=client_data["money"],
            car=client_data["car"]
        )
        clients[name] = client
    return clients


def create_shops(data: IO) -> dict:
    shops = {}
    for shop_data in data["shops"]:
        name = shop_data["name"]
        shop = Shop(
            name=name,
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops[name] = shop
    return shops
