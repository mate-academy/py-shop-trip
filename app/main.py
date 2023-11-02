import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    fname = "C:\\Users\\lisov\\PycharmProjects\\py-shop-trip\\app\\config.json"
    with open(fname, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    shops = []
    for shop in data["shops"]:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))

    for customer in data["customers"]:
        customer_cur = Customer(customer["name"], customer["product_cart"],
                                customer["location"], customer["money"],
                                customer["car"])
        print(f"{customer_cur.name} has {customer_cur.money} dollars")

        costs_min = {"shop": "", "cost": 0}
        for shop in shops:
            cost_shop = (customer_cur.cost_trip_shop(shop.location, fuel_price)
                         + customer_cur.cost_product_shop(shop.products))

            print(f"{customer_cur.name}'s trip to the {shop.name}"
                  f" costs {round(cost_shop, 2)}")

            if not costs_min["shop"] or cost_shop < costs_min["cost"]:
                costs_min["shop"] = shop
                costs_min["cost"] = cost_shop

        if costs_min["cost"] > customer_cur.money:
            print(f"{customer_cur.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        print(f"{customer_cur.name} rides to {costs_min['shop'].name}\n")

        costs_min["shop"].print_check(customer_cur.name,
                                      customer_cur.product_cart)

        print(f"{customer_cur.name} rides home")

        customer_cur.money = round((customer_cur.money - costs_min["cost"]), 2)
        print(f"{customer_cur.name} now has {customer_cur.money} dollars\n")
