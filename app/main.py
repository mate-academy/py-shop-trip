import json

from app.customer import Customer
from app.shop import Shop


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price: float = data["FUEL_PRICE"]
    customers: list = data["customers"]
    shops: list = data["shops"]

    for index, customer in enumerate(customers):
        name, product_cart, location, money, car = customer.values()
        customer = Customer(name, product_cart, location, money, car)
        customers[index] = customer

    for index, shop in enumerate(shops):
        name, location, products_cost = shop.values()
        shop = Shop(name, location, products_cost)
        shops[index] = shop

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_trip = customer.find_cheapest_trip_to_shop(shops, fuel_price)
        if customer.money < cheapest_trip["cost"]:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_trip['shop'].name}\n")
            customer.ride_to_shop(cheapest_trip)
            print(f"{customer.name} now has {customer.money} dollars\n")
