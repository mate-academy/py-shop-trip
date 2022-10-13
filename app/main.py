import json

from pathlib import Path

from app.get_receipt import get_receipt
from app.customer_info import get_info, print_info, choose_the_cheapest_shop


BASE_DIR = Path(__file__).resolve().parent


def shop_trip():

    with open(BASE_DIR / "config.json", "r") as file:
        data = json.load(file)

    for customer in data["customers"]:

        print(f"{customer['name']} has {customer['money']} dollars")

        customer_info = get_info(customer, data)
        print_info(customer_info)
        shop = choose_the_cheapest_shop(customer, customer_info, data)

        if customer_info["has_enough_money"]:
            get_receipt(customer, shop)
