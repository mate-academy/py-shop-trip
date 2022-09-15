from app.customer.customer import Customer
from app.distance_shop import distance_shop
import json
from app.shops.shop import Shop
from app.shopping_cart import shopping_cart_count, shopping_cart
from datetime import datetime


def shop_trip():
    with open("../app/config.json") as f:
        content = json.load(f)

    for person in content["customers"]:
        customer = Customer(person["name"], person["product_cart"],
                            person["location"], person["money"],
                            person["car"])

        print(f"{customer.name} has {customer.money} dollars")

        best_store = None
        best_store_price = 0
        final_cost = 0

        for place in content["shops"]:
            shop = Shop(place["name"], place["location"], place["products"])

            two_way_cost = distance_shop(shop.location,
                                         customer.location,
                                         customer.car.fuel_consumption,
                                         content["FUEL_PRICE"])
            price_cart = shopping_cart_count(shop.products, customer.products)
            final_price = round(two_way_cost + price_cart, 2)
            print(f"{customer.name}'s trip to the {shop.name} costs {final_price}")
            if final_price < best_store_price or best_store_price == 0:
                best_store_price = final_price
                best_store = shop
                final_cost = price_cart

        if customer.money < best_store_price:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
            continue
        else:
            print(f"{customer.name} rides to {best_store.name}\n")

        date = datetime(2021, 1, 4, 12, 33, 41)
        time = date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time}\n"
              f"Thanks, {customer.name}, for you purchase!")
        shopping_cart(best_store.products, customer.products)
        print(f"Total cost is {final_cost} dollars\n"
              f"See you again!\n")

        money_left = customer.money - best_store_price
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {money_left} dollars\n")


shop_trip()
