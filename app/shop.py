from dataclasses import dataclass
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
    return sum(
        product.get(key, 0) * value for
        key, value in customer_product.items()
    )


def make_a_receipt(
        customer_name: str,
        shops_inst: dict,
        product_cart: dict,
        date_time: str
) -> None:

    print(f"Date: {date_time}")
    print(f"Thanks, {customer_name}, for your purchase!")
    print("You have bought: ")

    prod = {
        "milk": product_cart["milk"] * shops_inst["milk"],
        "bread": product_cart["bread"] * shops_inst["bread"],
        "butter": product_cart["butter"] * shops_inst["butter"]
    }
    total = prod["milk"] + prod["bread"] + prod["butter"]
    print(f"{product_cart['milk']} milks for {prod['milk']} dollars")
    print(f"{product_cart['bread']} breads for {prod['bread']} dollars")
    print(f"{product_cart['butter']} butters for {prod['butter']} dollars")
    print(f"Total cost is {total} dollars")
    print("See you again!\n")
