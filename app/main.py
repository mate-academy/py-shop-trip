import datetime
import json


from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price, customers_list, shops_list = (
        config["FUEL_PRICE"],
        config["customers"],
        config["shops"]
    )
    customers = Customer.list_read(customers_list)
    shops = Shop.list_read(shops_list)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        shop_cost = None

        for shop in shops:
            total_cost = customer.car.trip_fuel_cost(shop.location, fuel_price)
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

        print(f"{customer.name} rides to {best_shop.name}\n")
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
