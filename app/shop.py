from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Shop:
    name: str
    location: list
    products: dict


def make_list_of_shop_instance(data: dict) -> List[Shop]:
    list_of_shops = []

    for shop_data in data:
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )
        list_of_shops.append(shop)
    return list_of_shops


def price_of_products(customer_product: dict, product: dict) -> int:
    price = 0
    for keys, value in customer_product.items():
        price = price + (product.get(keys) * value)
    return price


def make_a_receipt(
        customer_name: str,
        shops_inst: List[Shop],
        my_shop: str,
        product_cart: dict,
        location: list,
        date_time: datetime
) -> None:

    print(f"Date: {date_time}")
    print(f"Thanks, {customer_name}, for your purchase!")
    print("You have bought: ")
    prod = {
        "milk": 0,
        "bread": 0,
        "butter": 0,
        "total": 0
    }
    for shop in shops_inst:
        if my_shop == shop.name:
            prod["milk"] = product_cart["milk"] * shop.products["milk"]
            prod["bread"] = product_cart["bread"] * shop.products["bread"]
            prod["butter"] = product_cart["butter"] * shop.products["butter"]
    prod["total"] = prod["milk"] + prod["bread"] + prod["butter"]

    print(f"{product_cart['milk']} milks for {prod['milk']} dollars")
    print(f"{product_cart['bread']} breads for {prod['bread']} dollars")
    print(f"{product_cart['butter']} butters for {prod['butter']} dollars")
    print(f"Total cost is {prod['total']} dollars")
    print("See you again!\n")
