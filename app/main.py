import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as f:
        datas = json.load(f)

    fuel_price = datas["FUEL_PRICE"]

    customer_inst = [Customer(**customer) for customer in datas["customers"]]

    shop_inst = [Shop(**shop) for shop in datas["shops"]]

    for customer in customer_inst:
        print(f"{customer.name} has {customer.money} dollars")

        lowest_spent = 0
        flag = True

        for shop in shop_inst:
            if shop.is_all_product_in_shop(customer):
                money_spent = customer.car.cost_trip(
                    customer, shop, fuel_price
                )
                if flag:
                    lowest_spent = money_spent
                    lowest_shop_inst = shop
                    flag = False
                else:
                    if money_spent < lowest_spent:
                        lowest_spent = money_spent
                        lowest_shop_inst = shop

        if customer.money <= lowest_spent:
            print(
                f"{customer.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            continue

        customer.customer_to_shop(lowest_shop_inst)
        lowest_shop_inst.purchase(customer)
        customer.customer_to_home(lowest_spent)
