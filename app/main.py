import json
import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    input_data = json.load(open("app/config.json", "r"))

    fuel_price, customers, shops =\
        input_data["FUEL_PRICE"], input_data["customers"], input_data["shops"]

    customers = Customer.constructor(customers)
    shops = Shop.list_constructor(shops)

    for customers in customers:
        print(f"{customers.name} has {customers.money} dollars")
        best_shop = None
        shop_cost = None

        for shop in shops:
            total_cost = customers.car.fuel_price(shop.location, fuel_price)
            total_cost += shop.total_price(customers.product_cart)

            print(
                f"{customers.name}'s trip to the "
                f"{shop.name} costs {total_cost}"
            )

            if shop_cost is None or shop_cost > total_cost:
                best_shop = shop
                shop_cost = total_cost

        if customers.money < shop_cost:
            print(
                f"{customers.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
            continue

        customers.money -= shop_cost

        print(f"{customers.name} rides to {best_shop}\n")
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime(f'%d/%m/%Y %H:%M:%S')}"
        )
        print(
            f"Thanks, {customers.name}, for you purchase!\nYou have bought: "
        )

        best_shop.buy_product(customers.product_cart)

        print(
            f"{customers.name} rides home\n"
            f"{customers.name} now has {customers.money} dollars\n"
        )
