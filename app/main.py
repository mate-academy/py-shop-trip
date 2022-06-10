import json
from pathlib import Path

from app.customer import Customer
from app.shop import Shop

BASE_DIR = Path(__file__).resolve().parent


def shop_trip():
    fuel_price, customers, shops = create_customers_and_shops()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.find_better_price(shops, fuel_price)
        for shop, price in customer.trips.items():
            print(f"{customer.name}'s trip to the {shop} costs {price}")
        if customer.money > min(customer.trips.values()):
            print(f"{customer.name} rides to {customer.cheapest_shop.name}\n")
            customer.do_shopping()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min(customer.trips.values())} dollars\n")
        else:
            print(f"{customer.name}"
                  f" doesn't have enough money to make purchase in any shop")


def create_customers_and_shops():
    with open(BASE_DIR / "config.json", "r") as f:
        data = json.load(f)

    FUEL_PRICE = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    for index, customer in enumerate(customers):
        name, product_cart, location, money, car = customer.values()
        customer = Customer(name, product_cart, location, money, car)
        customers[index] = customer

    for index, shop in enumerate(shops):
        name, location, prices = shop.values()
        shop = Shop(name, location, prices)
        shops[index] = shop

    return FUEL_PRICE, customers, shops


shop_trip()
