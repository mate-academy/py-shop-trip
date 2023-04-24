import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as opened_json_file:
        config_file = json.load(opened_json_file)
    customers_list = list()
    shops_list = list()
    fuel_price = config_file["FUEL_PRICE"]
    for customer in config_file["customers"]:
        customers_list.append(
            Customer(customer["name"],
                     customer["product_cart"],
                     customer["location"],
                     customer["money"],
                     customer["car"]
                     )
        )
    for shop in config_file["shops"]:
        shops_list.append(
            Shop(shop["name"],
                 shop["location"],
                 shop["products"]
                 )
        )
    for customer in customers_list:
        chosen_shop = customer.choose_shop_or_stay_home(shops_list, fuel_price)
        if chosen_shop:
            chosen_shop.print_check(customer.name, customer.product_cart)
            customer.ride_home()

