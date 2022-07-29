import json

from app.Customer import Customer
from app.Shop import Shop


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)
        shop_list = []
        for shop in data['shops']:
            shop_obj = Shop(shop['name'], shop['location'], shop['products'])
            shop_list.append(shop_obj)
        for customer in data['customers']:
            customer_obj = Customer(customer['name'], customer['product_cart'],
                                    customer['location'],
                                    customer['location'], customer['money'],
                                    customer['car'], data['FUEL_PRICE'])
            customer_obj.find_cheapest_shop_and_print_info(shop_list)


shop_trip()
