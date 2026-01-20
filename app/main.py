import json
import datetime

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(**customer["car"])
        )
        for customer in data["customers"]
    ]

    shops = [Shop(**shops) for shops in data["shops"]]

    for customer in customers:
        min_cost = float("inf")
        choose_shop = Shop
        total_product_price = 0
        print(customer.have_money())

        for shop in shops:
            price = customer.total_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {price}")

            if price < min_cost:
                min_cost = price
                choose_shop = shop
        if min_cost > customer.money:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        else:
            print(f"{customer.name} rides to {choose_shop.name}\n")

        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought:")

        for product, quantity in customer.product_cart.items():
            if product in choose_shop.products:
                product_price = quantity * choose_shop.products[product]
                if (isinstance(product_price, float)
                        and product_price.is_integer()):
                    product_price = int(product_price)
                print(f"{quantity} {product}s for {product_price} dollars")
                total_product_price += product_price
            else:
                raise KeyError(f"There is no {product} in {choose_shop.name}")

        print(f"Total cost is {total_product_price} dollars\n"
              "See you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has {customer.money - min_cost} dollars\n")
