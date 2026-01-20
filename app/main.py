import os
import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:

    with open(os.getcwd() + "/app/config.json", "r") as file:
        info = json.load(file)

    buyers = info["customers"]
    stores = info["shops"]
    fuel_price = info["FUEL_PRICE"]
    out = """"""
    for buyer in buyers:
        customer = Customer(
            buyer["name"],
            buyer["product_cart"],
            buyer["location"],
            buyer["money"]
        )
        car = Car(
            brand=buyer["car"]["brand"],
            fuel_consumption=buyer["car"]["fuel_consumption"]
        )
        out += customer.money_amount()
        cost_in_all_shops = {}
        for store in stores:
            shop = Shop(
                store["name"],
                store["location"],
                store["products"]
            )
            cost_in_one_shop = (
                customer.cost_of_products_in_shop(shop.shop_products)
            )
            cost_of_fuel = (
                car.liters_needed(customer.location, shop.shop_location)
                * fuel_price
            )
            sum_shop_and_fuel_cost = round(cost_in_one_shop + cost_of_fuel, 2)
            out += (f"{customer.name}'s trip to the {shop.shop_name} "
                    f"costs {sum_shop_and_fuel_cost}\n")
            cost_in_all_shops[shop.shop_name] = sum_shop_and_fuel_cost
        min_cost_key = min(
            cost_in_all_shops, key=lambda k: cost_in_all_shops[k]
        )
        if customer.money > cost_in_all_shops[min_cost_key]:
            out += f"{customer.name} rides to {min_cost_key}\n\n"
            index_of_the_right_shop = 0
            for index, store in enumerate(stores):
                if store["name"] == min_cost_key:
                    index_of_the_right_shop = index

            min_bill_shop = Shop(
                shop_name=stores[index_of_the_right_shop]["name"],
                shop_location=stores[index_of_the_right_shop]["location"],
                shop_products=stores[index_of_the_right_shop]["products"]
            )
            out += min_bill_shop.bill(customer.name, customer.products)
            customer.change_location(min_bill_shop.shop_location)
            amount_left = customer.money - cost_in_all_shops[min_cost_key]
            out += "\n"
            out += f"{customer.name} rides home\n"
            out += f"{customer.name} now has {amount_left} dollars\n\n"

        else:
            out += (f"{customer.name} doesn't have enough money "
                    f"to make a purchase in any shop")
    print(out)
