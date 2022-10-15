import json

from app.customers.customer import Customer
from app.purchases.purchase import perform_purchase_of_products
from app.shops.shop import Shop


def get_info_from_json():
    with open("app/config.json", "r") as json_file:
        purchases_info = json.load(json_file)
    return purchases_info


def shop_trip():
    purchase_info = get_info_from_json()

    fuel_price = purchase_info["FUEL_PRICE"]

    customers = [
        Customer.get_customer_instance(customer)
        for customer in purchase_info["customers"]
    ]

    shops = [
        Shop.get_shop_instance(shop)
        for shop in purchase_info["shops"]
    ]

    for customer in customers:
        perform_purchase_of_products(customer, shops, fuel_price)
