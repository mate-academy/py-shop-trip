import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as data_file:
        config = json.load(data_file)

    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]
    for customer in customers:
        customer_home = customer.location
        best_choice_shop = customer.shop_selection(shops)
        if best_choice_shop:
            best_choice_shop.cashiers_check(customer)
            customer.location = customer_home
            customer.after_shopping(best_choice_shop)


shop_trip()
