import datetime
import json

from app.package.cost_of_the_trip import get_distance_cost
from app.package.create_instance import create_shop, create_customer
from app.package.shopping import buy_products


def shop_trip() -> None:
    with open("app/config.json", "r") as source_file:
        data_from_file = json.load(source_file)

    fuel_price = data_from_file["FUEL_PRICE"]

    customers = [create_customer(customer)
                 for customer in data_from_file["customers"]]
    shops = [create_shop(shop) for shop in data_from_file["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        store_prices = buy_products(customer=customer, shops=shops)
        total_cost, shop_index = get_distance_cost(
            customer=customer,
            shops=shops,
            car=customer.car,
            fuel_price=fuel_price,
            store_prices=store_prices
        )

        if total_cost < customer.money:
            current_time = datetime.datetime.now()
            print("Date: " + current_time.strftime("%d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for items, i in zip(customer.product_cart.items(), range(3)):
                print(f"{items[1]} {items[0]}s for "
                      f"{store_prices[shop_index][i]} dollars")

            print(f"Total cost is {store_prices[shop_index][3]} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - total_cost} dollars\n")
