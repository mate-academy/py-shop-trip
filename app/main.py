import json
import os

from app.customer import Customer
from app.shop import Shop
from app.car import fuel_price, drive_to_shop, drive_to_home


def shop_trip() -> None:

    os.chdir("C:\\Users\\kolom\\python-course\\py-shop-trip\\app\\")

    with open("config.json") as file:
        file_info = json.load(file)

    liter_price = file_info["FUEL_PRICE"]
    customers_info = file_info["customers"]
    shops_info = file_info["shops"]
    customers = []
    shops = []

    for person in customers_info:
        car = {
            "brand": person["car"]["brand"],
            "fuel_consumption": person["car"]["fuel_consumption"]
        }
        customers.append(
            Customer(
                person["name"],
                person["product_cart"],
                person["location"],
                person["money"],
                car
            )
        )

    for shop in shops_info:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        prices_dict = {}

        for store in shops:
            total_price = round(
                store.products_price(customer) + fuel_price(
                    store, customer, liter_price
                ),
                2
            )
            prices_dict[total_price] = store
            print(
                f"{customer.name}'s trip "
                f"to the {store.name} costs {total_price}"
            )

        cheapest_price = min(prices_dict)
        cheapest_store = prices_dict[cheapest_price]

        if not customer.has_enough_money(cheapest_price):
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            return

        drive_to_shop(cheapest_store, customer)
        cheapest_store.print_purchase_receipt(customer)
        drive_to_home(customer)
        customer.money -= cheapest_price

        print(f"{customer.name} now has {customer.money} dollars\n")


if __name__ == "__main__":
    shop_trip()
