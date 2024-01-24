import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        data = json.load(file)

    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        best_shop, price = customer.find_best_shop(shops, data["FUEL_PRICE"])
        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            best_shop.make_shopping_proces(customer)
            print(f"{customer.name} rides home")
            customer.location = customer.home
            print(f"{customer.name} now has {customer.money - price} "
                  f"dollars\n")


shop_trip()
