import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(**shop) for shop in config["shops"]
    ]
    customers = [
        Customer(**customer) for customer in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        expenses = {}
        for shop in shops:
            expenses[shop] = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {expenses[shop]}")

        cheapest_trip = min(expenses, key=expenses.get)

        if customer.money < expenses[cheapest_trip]:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {cheapest_trip.name}\n")

        customer.location = cheapest_trip.location
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought:")
        total_product_costs = 0
        for product, amount in customer.product_cart.items():
            price = amount * cheapest_trip.products[product]
            str_price = ("{:.2f}".format(price)
                         .rstrip("0").rstrip("."))
            total_product_costs += price
            print(f"{amount} {product}s for {str_price} dollars")
        print(f"Total cost is {total_product_costs} dollars\n"
              f"See you again!\n")

        customer.money -= expenses[cheapest_trip]
        customer.location = cheapest_trip.location
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")
