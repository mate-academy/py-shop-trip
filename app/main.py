import json
from app.customer import Customer
from app.shop import Shop


with open("app/config.json", "r") as file:
    data = json.load(file)

FUEL_PRICE = data["FUEL_PRICE"]

customers = [Customer(customer) for customer in data["customers"]]
shops = [Shop(shop) for shop in data["shops"]]


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_, expenses = customer.select_shop(FUEL_PRICE, shops)

        if customer.money < expenses["total"]:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {shop_.name}\n")
            customer.go_to_shop(shop_, expenses)
