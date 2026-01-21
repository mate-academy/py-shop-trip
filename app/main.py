import json

from app.car import Car
from app.customer import Customer
from app.product import Products
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
    customers = [Customer(customer["name"],
                          Products(**customer["product_cart"]),
                          customer["location"],
                          customer["money"],
                          Car(**customer["car"]))
                 for customer in data["customers"]]
    shops = [Shop(shop["name"],
                  Products(**shop["products"]),
                  shop["location"]) for shop in data["shops"]]

    fuel_price = data["FUEL_PRICE"]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        all_prices = {}
        for i in range(len(shops)):
            pay_for_trip = customer.all_cost(shops[i], fuel_price)
            print(f"{customer.name}'s trip "
                  f"to the {shops[i].name} costs {pay_for_trip}")
            all_prices[i] = pay_for_trip
        index_min_price = min(all_prices, key=lambda k: all_prices[k])
        if customer.have_enough_money(all_prices[index_min_price]):
            shop = shops[index_min_price]
            print(f"{customer.name} rides to {shop.name}")
            customer.print_check(shop)
            print(f"{customer.name} rides home")

            customer.pay_for_groceries(all_prices[index_min_price])
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
