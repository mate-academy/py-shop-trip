import json
import os
import datetime
from app.shop import Shop
from app.customer import Customer
from typing import List, Dict, Tuple


def load_config_data(file_path: str) -> Dict:
    with open(file_path, "r") as file:
        return json.load(file)


def calculate_customer_costs(customers: List[Customer],
                             shops: List[Shop],
                             fuel_price: float
                             ) -> str:
    total_result_shopping = ""

    for customer in customers:
        cost_in_shops = [
            (shop.total_costing(customer=customer,
                                fuel_price=fuel_price), shop)
            for shop in shops
        ]

        total_result_shopping += (f"{customer.name} has "
                                  f"{customer.money} dollars\n")

        for cost, shop in cost_in_shops:
            total_result_shopping += (f"{customer.name}'s "
                                      f"trip to the {shop.name}"
                                      f" costs {cost}\n")

        select_shop = min(cost_in_shops, key=lambda x: x[0])

        if select_shop[0] > customer.money:
            total_result_shopping += (f"{customer.name} doesn't "
                                      f"have enough money to "
                                      f"make a purchase in any shop\n")
        else:
            total_result_shopping += process_purchase(select_shop, customer)

    return total_result_shopping


def format_shop_purchase(select_shop: Tuple[float, Shop],
                         customer: Customer
                         ) -> str:
    today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    formatted_purchase = f"{customer.name} rides to {select_shop[1].name}\n\n"
    formatted_purchase += f"Date: {today}\n"
    formatted_purchase += f"Thanks, {customer.name}, for your purchase!\n"
    formatted_purchase += "You have bought: \n"

    shop_basket = select_shop[1].basket_collection(customer=customer)

    for product in shop_basket:
        count_product, price_product = shop_basket[product]
        price_product = (int(price_product)
                         if price_product % int(price_product) == 0
                         else price_product)

        formatted_purchase += (f"{count_product} {product}s "
                               f"for {price_product} dollars\n")

    total_cost_product = select_shop[1].calculate_cost_products(
        customer=customer)
    formatted_purchase += f"Total cost is {total_cost_product} dollars\n"
    formatted_purchase += "See you again!\n\n"

    customer.money -= select_shop[0]
    formatted_purchase += f"{customer.name} rides home\n"
    formatted_purchase += (f"{customer.name} now "
                           f"has {customer.money} dollars\n\n")

    return formatted_purchase


def process_purchase(select_shop: Tuple[float, Shop],
                     customer: Customer
                     ) -> str:
    return format_shop_purchase(select_shop, customer)


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    data = load_config_data(path)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    total_result_shopping = calculate_customer_costs(customers,
                                                     shops,
                                                     fuel_price)
    print(total_result_shopping[:-1])


if __name__ == "__main__":
    shop_trip()
