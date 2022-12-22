import json

from app.customer import Customers
from app.shop import Shops


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = Customers.add_customer(data["customers"])
        shops = Shops.add_shop(data["shops"])

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cost, cheapest_shop, purchase_note = \
            customer.count_cost(customer, shops, fuel_price)

        if cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}"
                  f"\n")
            cheapest_shop.customer_purchase(customer.name, purchase_note)
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has {customer.money - cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
