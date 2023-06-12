from math import sqrt
import datetime
import json


def possibilities(customer_name, shop_dict, money):
    if min(shop_dict) <= money:
        print(f"{customer_name} rides to {shop_dict[min(shop_dict)]}\n")
        return min(shop_dict)
    else:
        print(f"{customer_name} doesn't have enough "
              f"money to make purchase in any shop")


def receipt(customer_name, product_cart, products):
    total = 0
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {now}")
    print(f"Thanks, {customer_name}, for you purchase!\n"
          f"You have bought: ")
    for product, price in zip(product_cart, products):
        product_amount = product_cart[product]
        product_price = products[price]
        print(f"{product_amount} {product}s"
              f" for {product_price * product_amount} dollars")
        total += product_price * product_amount
    print(f"Total cost is {total} dollars")
    print("See you again!")
    print(f"{customer_name} rides home")


def shop_trip():
    with open("app/config.json", "r") as source:
        config = json.load(source)

        for customer in config["customers"]:
            customer_name = customer["name"]
            start = customer["location"]
            fuel_consumption = customer["car"]['fuel_consumption']
            product_cart = customer["product_cart"]
            money = customer["money"]
            shop_dict = dict()
            print(f"{customer_name} has {money} dollars")

            for shop in config["shops"]:
                end = shop["location"]
                shop_name = shop["name"]
                products = shop["products"]
                distance = 0
                for i in (0, 1):
                    distance += (end[i] - start[i]) ** 2
                distance = round(sqrt(distance), 2)
                km_cost = round(fuel_consumption * config["FUEL_PRICE"], 2)
                fuel_cost = round(round(km_cost / 100, 2) * distance, 2)
                products_cost = sum(i * j for i, j in
                                    zip(product_cart.values(),
                                        products.values()))
                cost = round(fuel_cost * 2 + products_cost, 2)
                print(f"{customer_name}'s trip"
                      f" to the {shop_name} costs {cost}")
                shop_dict[cost] = shop_name
            price = possibilities(customer_name, shop_dict, money)
            if price:
                for shop in config["shops"]:
                    if shop_dict[price] == shop["name"]:
                        receipt(customer_name, product_cart, shop["products"])
                        print(f"{customer_name} now"
                              f" has {money - price} dollars\n")
