import json
from app.customer import Customer
from app.shop import Shop
import app.helping_tool as helping_tool


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config_json = json.load(config)
    fuel_price = config_json["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config_json["customers"]]
    shops = [Shop(**shops) for shops in config_json["shops"]]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheaper_shop = None
        cheaper_shop_name = None

        for shop in shops:
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{helping_tool.trip_and_shop_price(
                      shop, customer, fuel_price)}")
            if cheaper_shop is None:
                cheaper_shop = helping_tool.trip_and_shop_price(
                    shop, customer, fuel_price)
                cheaper_shop_name = shop
            elif cheaper_shop > helping_tool.trip_and_shop_price(
                    shop, customer, fuel_price):
                cheaper_shop = helping_tool.trip_and_shop_price(
                    shop, customer, fuel_price)
                cheaper_shop_name = shop
        if cheaper_shop > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheaper_shop_name.name}\n")
            cheaper_shop_name.receipt(customer)
            customer.spend_money(cheaper_shop)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")


shop_trip()
