import json
import datetime

from app.shop import Shop
from app.customers import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        all_data = json.load(file)

    shops = [Shop(*item.values()) for item in all_data["shops"]]
    customers = [
        Customer(*item.values())
        for item
        in all_data["customers"]
    ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        list_trip = []
        for shop in shops:
            coast_cart = shop.cost_products(customer.product_cart)
            distance = customer.distance(shop.location)
            coast_trip = (customer.car.amount_of_fuel(distance)
                          * all_data["FUEL_PRICE"])
            full_coast = round((coast_cart + coast_trip), 2)
            list_trip.append([full_coast, shop])
            print(
                f"{customer.name}'s trip to the"
                f" {shop.name} costs {full_coast}")

        best_coast = min(list_trip)[0]
        best_shop = min(list_trip)[1]

        if customer.money >= best_coast:
            print(f"{customer.name} rides to {best_shop.name}\n")
            now = datetime.datetime.now()
            formatted_date = now.strftime("Date: %d/%m/%Y %H:%M:%S")
            print(formatted_date)

            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            cost_all_products = 0
            for product, quantity in customer.product_cart.items():
                cost_each_product = (
                    best_shop.products[product]
                    * customer.product_cart[product]
                )
                if cost_each_product == int(cost_each_product):
                    cost_each_product = int(cost_each_product)
                cost_all_products += cost_each_product
                print(
                    f"{quantity} {product}s for"
                    f" {cost_each_product} dollars")
            print(
                f"Total cost is"
                f" {cost_all_products} dollars"
            )
            print("See you again!\n")

            print(f"{customer.name} rides home")
            customer.money = customer.money - best_coast
            print(
                f"{customer.name} now has"
                f" {customer.money} dollars\n")

        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
