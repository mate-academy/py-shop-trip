import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file_in:
        data = json.load(file_in)

    customers: list[Customer] = []
    shops: list[Shop] = []

    Car.FUEL_PRICE = data["FUEL_PRICE"]

    for customer in data["customers"]:
        customers.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"], customer["car"]["fuel_consumption"]
            )
        ))

    for shop in data["shops"]:
        shops.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_to_ride, cost_for_trip_shop = customer.choose_min_cost_shop(shops)
        if customer.has_enough_money(cost_for_trip_shop):
            customer.ride_to_shop(shop_to_ride)
            print()
            customer.buy_products(shop_to_ride)
            print()
            customer.ride_back_home(shop_to_ride)
            print(f"{customer.name} now has {customer.money:.2f} dollars")
            print()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


shop_trip()
