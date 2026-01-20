import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)
        fuel_price = config["FUEL_PRICE"]
        customers = [
            Customer(**customer)
            for customer in config["customers"]
        ]
        shops = [
            Shop(**shop)
            for shop in config["shops"]
        ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        expenses = {}
        for shop in shops:
            expenses[shop] = customer.calculate_trip_expenses(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {expenses[shop]}")
        cheapest_shop = min(expenses, key=expenses.get)
        if customer.money < expenses[cheapest_shop]:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {cheapest_shop.name}\n")

        customer.location = cheapest_shop.location
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought:")
        total_price = 0
        for product, amount in customer.product_cart.items():
            price_for_product = amount * cheapest_shop.products[product]
            str_price = ("{:.2f}".format(price_for_product)
                         .rstrip("0").rstrip("."))
            total_price += price_for_product
            print(f"{amount} {product}s for {str_price} dollars")
        print(f"Total cost is {total_price} dollars\n"
              "See you again!\n")

        customer.location = customer.home
        customer.money -= expenses[cheapest_shop]
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")
