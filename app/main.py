from app.customer.customer import Customer
from app.distance_shop import distance_shop
import json
from app.shops.shop import Shop
from app.shopping_cart import shopping_cart_count, shopping_cart
from datetime import datetime


def shop_trip():
    with open("config.json") as f:
        content = json.load(f)

    for person in content["customers"]:
        customer = Customer(person["name"], person["product_cart"],
                            person["location"], person["money"],
                            person["car"])

        print(f"{customer.name} has {customer.money} dollars")

        best_store = ""
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
            print(f"Bob's trip to the {shop.name} costs {final_price}")
            if final_price < best_store_price or best_store_price == 0:
                best_store_price = final_price
                best_store = shop
                final_cost = price_cart

        if customer.money < best_store_price:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop\n")
            continue
        else:
            print(f"{customer.name} rides to {best_store.name}\n")

        now = datetime.now()
        time = now.strftime("%Y/%m/%d %H:%M:%S")
        print(time)
        shopping_cart(best_store.products, customer.products)
        print(f"Total cost is {final_cost} dollars\n"
              f"See you again!\n")

        money_left = customer.money - best_store_price
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {money_left} dollars\n")


shop_trip()
