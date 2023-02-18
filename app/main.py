import json
from app.logical import *


def shop_trip() -> None:
    with open("config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer.get_customer_info(customer) for customer in data["customers"]
    ]
    shops = [Shop.get_shop_info(shop) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop, cheapest_trip, cheapest_total = (
            find_cheapest_shop_and_trip(customer, shops, fuel_price)
        )
        if customer.money > cheapest_trip + cheapest_total:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            get_check(customer, cheapest_shop)
            print(
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{customer.money - cheapest_total} dollars\n"
            )
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")


if __name__ == "__main__":
    shop_trip()
