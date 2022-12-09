from app.Shop import Shop
from app.Customer import Customer
import json

with open("app/config.json", "r") as data_customers:
    data = json.load(data_customers)


def shop_trip() -> None:
    for item in data["customers"]:
        cheap_shop = {}
        customer_info = (
            item["name"],
            item["product_cart"],
            item["location"],
            item["money"],
            item["car"],
            data["FUEL_PRICE"],
        )

        customer = Customer(*customer_info)
        print(customer.get_info())
        for each_shop in data["shops"]:
            shop = Shop(
                each_shop["name"],
                each_shop["location"],
                each_shop["products"],
                *customer_info,
            )
            cheap_shop[shop.shop_name] = (
                shop.calculate(customer) + shop.get_fuel_price()
            )
            print(
                f"{customer.person_name}'s trip to the "
                f"{shop.shop_name} costs "
                f"{shop.calculate(customer) + shop.get_fuel_price()}"
            )
        cheap_shop = sorted(cheap_shop.items(), key=lambda x: x[1])[0]
        if cheap_shop[1] >= customer.person_money:
            print(
                f"{customer.person_name} "
                f"doesn't have enough money to make purchase in any shop"
            )
        else:
            print(f"{customer.person_name} rides to {cheap_shop[0]}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.person_name}, for you purchase!")
            print("You have bought: ")
            shop.info_buy(data["shops"], cheap_shop[0], customer)
            print(f"{customer.person_name} rides home")
            print(
                f"{customer.person_name} now has "
                f"{customer.person_money - cheap_shop[1]} dollars\n"
            )
