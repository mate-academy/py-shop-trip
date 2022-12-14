import json

from app.customer import Customers
from app.shop import Shops
from app.car import Car


def shop_trip():
    with open("config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = Customers.add_customer(data["customers"])
        shops = Shops.add_shop(data["shops"])

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost, cheapest_shop, purchase_note = customer.count_cost(customer, shops, fuel_price)
        print(purchase_note)
        if min_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}"
                  f"\n")
            cheapest_shop.customer_purchase(customer.name, purchase_note)
        else:
            print(f"{customer.name} doesn't have enough money to make purchase in any shop")






shop_trip()


