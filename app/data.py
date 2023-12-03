from typing import IO

from app.customer import Customer
from app.shops import Shop


def create_clients(data: IO) -> dict:
    clients = {
        client_data["name"]: Customer(**client_data)
        for client_data in data["customers"]
    }
    return clients


def create_shops(data: IO) -> dict:
    shops = {
        shop_data["name"]: Shop(**shop_data)
        for shop_data in data["shops"]}
    return shops
