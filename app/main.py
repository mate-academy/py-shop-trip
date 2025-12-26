import json
import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as f:
        all_data = json.load(f)
    fuel_price = all_data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in all_data["customers"]]
    shops = [Shop(shop) for shop in all_data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheaper_shop = {}
        cheaper_trip = {}
        for shop in shops:
            all_cost = customer.cost_trip(fuel_price, shop.location) +\
                shop.product_customer(customer.product_cart)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {all_cost}")
            cheaper_shop[all_cost] = shop.name
            if customer.money >= all_cost:
                cheaper_trip[all_cost] = shop
        if not cheaper_trip:
            print(f"{customer.name} "
                  f"doesn't have enough money to make purchase in any shop")
            return

        print(f"{customer.name} rides to "
              f"{cheaper_shop[min(cheaper_shop.keys())]}\n")
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for you purchase!\nYou have bought: ")
        print(cheaper_trip[min(cheaper_shop.keys())].receipt(customer))
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - min(cheaper_shop.keys())} dollars\n")
