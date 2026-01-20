import datetime
import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config:
        data = json.load(config)
        fuel_price = data["FUEL_PRICE"]
        customers = data["customers"]
        shops = data["shops"]
    list_customers = []
    for customer in customers:
        list_customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ))
    list_shops = []
    for shop in shops:
        list_shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))

    for customer in list_customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_dict = {}
        for shop in list_shops:
            distance = customer - shop
            gasoline = ((distance) * 2 / 100
                        * customer.car["fuel_consumption"] * fuel_price)
            products_cost = sum(
                [value * shop.products[key]
                 for key, value in customer.product_cart.items()]
            )
            cost = round(gasoline + products_cost, 2)
            shop_dict[cost] = shop.name
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        min_cost = min([key for key in shop_dict.keys()])
        if customer.money < min_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            chosen_shop = [shop for shop in list_shops
                           if shop.name == shop_dict[min_cost]]
            chosen_shop = chosen_shop[0]
            print(f"{customer.name} rides to {chosen_shop.name}")
            gasoline = round(
                (customer - chosen_shop) * 2 / 100
                * customer.car["fuel_consumption"] * fuel_price,
                2
            )
            customer.location = chosen_shop.location
            print()
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            products = 0
            for key, value in customer.product_cart.items():
                prod_cost = value * chosen_shop.products[key]
                products += prod_cost
                if value > 1:
                    print(
                        f"{value} {key}s for "
                        f"{str(prod_cost).rstrip('0').rstrip('.')} dollars"
                    )
                else:
                    print(
                        f"{value} {key} for "
                        f"{str(prod_cost).rstrip('0').rstrip('.')} dollars"
                    )
            print(f"Total cost is {products} dollars")
            print("See you again!")
            print()
            customer.money -= products + gasoline
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars")
            print()
