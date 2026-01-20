import json
import os

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in data["shops"]]
    customers = [Customer(**customer) for customer in data["customers"]]

    result_shopping = ""

    for customer in customers:
        cost_in_shops = [
            (shop.total_costing(
                customer=customer,
                fuel_price=fuel_price
            ), shop)
            for shop in shops
        ]

        result_shopping += f"{customer.name} has {customer.money} dollars\n"

        for cost, shop in cost_in_shops:
            result_shopping += (f"{customer.name}'s trip to the "
                                f"{shop.name} costs {cost}\n")

        select_shop = sorted(cost_in_shops)[0]

        if select_shop[0] > customer.money:
            result_shopping += (f"{customer.name} doesn't have enough money "
                                f"to make a purchase in any shop\n")

        else:
            result_shopping += (f"{customer.name} rides to "
                                f"{select_shop[1].name}\n\n"
                                f"Date: 04/01/2021 12:33:41\n"
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

                result_shopping += (f"{count_product} {product}s "
                                    f"for {price_product} dollars\n")

            total_cost_product = select_shop[1].calculate_cost_products(
                customer=customer
            )
            result_shopping += (f"Total cost is {total_cost_product} dollars\n"
                                f"See you again!\n\n")

            customer.money -= select_shop[0]

            result_shopping += (f"{customer.name} rides home\n"
                                f"{customer.name} now has "
                                f"{customer.money} dollars\n\n")

    print(result_shopping[:-1])
