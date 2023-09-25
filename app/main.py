import json
import os

import datetime
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]
    total_result_shopping = ""

    for customer in customers:
        cost_in_shops = [
            (shop.total_costing(
                customer=customer,
                fuel_price=fuel_price
            ), shop)
            for shop in shops
        ]

        total_result_shopping += (f"{customer.name} has "
                                  f"{customer.money} dollars\n"
                                  )
        for cost, shop in cost_in_shops:
            total_result_shopping += (f"{customer.name}'s trip to the "
                                      f"{shop.name} costs {cost}\n")

        select_shop = min(cost_in_shops, key=lambda x: x[0])
        if select_shop[0] > customer.money:
            total_result_shopping += (f"{customer.name} doesn't have "
                                      f"enough money to make a purchase "
                                      f"in any shop\n")

        else:
            today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            total_result_shopping += (f"{customer.name} rides to "
                                      f"{select_shop[1].name}\n\n"
                                      f"Date: {today}\n"
                                      f"Thanks, {customer.name}, "
                                      f"for your purchase!\n"
                                      f"You have bought: \n")

            shop_basket = select_shop[1].basket_collection(customer=customer)

            for product in shop_basket:
                count_product = shop_basket[product][0]
                price_product = shop_basket[product][1]
                price_product = int(price_product) \
                    if price_product % int(price_product) == 0 \
                    else price_product
                total_result_shopping += (f"{count_product} {product}s "
                                          f"for {price_product} dollars\n")

            total_cost_product = select_shop[1].calculate_cost_products(
                customer=customer
            )
            total_result_shopping += (f"Total cost "
                                      f"is {total_cost_product} dollars\n"
                                      f"See you again!\n\n")

            customer.money -= select_shop[0]

            total_result_shopping += (f"{customer.name} rides home\n"
                                      f"{customer.name} now has "
                                      f"{customer.money} dollars\n\n")
    print(total_result_shopping[:-1])
