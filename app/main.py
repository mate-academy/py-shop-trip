import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data.get("FUEL_PRICE")

    customers = [Customer(customer) for customer in data.get("customers")]
    shops = [Shop(shop) for shop in data.get("shops")]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_, expenses = customer.select_shop(fuel_price, shops)

        if customer.money < expenses.get("total"):
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {shop_.name}\n")
            customer.go_to_shop(shop_, expenses)


shop_trip()
