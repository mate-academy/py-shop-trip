import json
import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    file = json.load(open("app/config.json", "r"))

    fuel_price, customers_list, shops_list = \
        file["FUEL_PRICE"], file["customers"], file["shops"]

    customers_list = Customer.constructor(customers_list)
    shops_list = Shop.list_constructor(shops_list)

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        shop_cost = None

        for index, shop in enumerate(shops_list):
            total_cost = customer.car.fuel_price(shop.location, fuel_price)
            total_cost += shop.total_price(customer.product_cart)

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_cost}"
            )

            if shop_cost is None or shop_cost > total_cost:
                best_shop = shop
                shop_cost = total_cost

        if customer.money < shop_cost:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
            continue

        customer.money -= shop_cost

        print(f"{customer.name} rides to {best_shop}\n")
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime(f'%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer.name}, for you purchase!\nYou have bought: ")

        best_shop.buy_product(customer.product_cart)

        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now has {customer.money} dollars\n"
        )
