from dataclasses import dataclass
import json

from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict



def make_list_of_shop_instance():
    with open("config.json", 'r') as file_data:
        data = json.load(file_data)

    list_of_shops = []

    for shop_data in data["shops"]:
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
        customer_name,
        shops_inst,
        my_shop,
        product_cart,
        location,
        date_time
):

    print(f"Date: {date_time}")
    print(f"Thanks, {customer_name}, for your purchase!")
    print("You have bought: ")
    product_dict = {
        "milk": 0,
        "bread": 0,
        "butter": 0,
        "total": 0
    }
    for shop in shops_inst:
        if my_shop == shop.name:
            location = shop.location
            product_dict["milk"] = product_cart["milk"] * shop.products["milk"]
            product_dict["bread"] = product_cart["bread"] * shop.products["bread"]
            product_dict["butter"] = product_cart["butter"] * shop.products["butter"]
    product_dict["total"] = product_dict["milk"] + product_dict["bread"] + product_dict["butter"]

    print(f"{product_cart['milk']} milks for {product_dict['milk']} dollars")
    print(f"{product_cart['bread']} breads for {product_dict['bread']} dollars")
    print(f"{product_cart['butter']} butters for {product_dict['butter']} dollars")
    print(f"Total cost is {product_dict['total']} dollars")
    print("See you again!\n")
