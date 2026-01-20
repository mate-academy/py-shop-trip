from app.car import Car
from app.customer import Customer
from app.shop import Shop
import json


def load_config() -> tuple[float, list[Customer], list[Shop]]:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(name=customer["name"],
                 product_cart=customer["product_cart"],
                 customer_location=customer["location"],
                 money=customer["money"],
                 car=Car(**customer["car"]))
        for customer in config["customers"]
    ]

    shops = [
        Shop(name=shop["name"],
             shop_location=shop["location"],
             products=shop["products"])
        for shop in config["shops"]
    ]

    return fuel_price, customers, shops


def print_purchase_receipt(customer: Customer, shop: Shop) -> None:
    customer.print_the_purchase_receipt(shop)
    print(f"Total cost is {customer.get_product_price(shop)} dollars")
    print("See you again!\n")


def shop_trip() -> None:
    fuel_price, customers, shops = load_config()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_cost = None
        cheapest_shop = None
        for shop in shops:
            trip_cost = customer.get_trip_price(fuel_price, shop)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
            if cheapest_cost is None or trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                cheapest_shop = shop
        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            customer.money -= cheapest_cost

            print_purchase_receipt(customer, cheapest_shop)

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
