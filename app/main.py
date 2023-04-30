import json

from app.customer import Customer
from app.shop import Shop
from app.print_user_info import print_user_info


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        user_and_shop_data = json.load(file)
    fuel_price = user_and_shop_data["FUEL_PRICE"]
    customers = [Customer.make_instance(customer) for customer
                 in user_and_shop_data["customers"]]
    shops = [Shop.make_instance(shop) for shop in user_and_shop_data["shops"]]
    is_first_customer = True
    for customer in customers:
        if not is_first_customer:
            print("")
        is_first_customer = False
        print_user_info(customer, shops, fuel_price)
