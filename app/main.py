import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        shopping_data = json.load(file)
    fuel_price = shopping_data["FUEL_PRICE"]
    customers_dict = {}
    shops_dict = {}
    for customer in shopping_data["customers"]:
        customers_dict[customer["name"]] = Customer(customer)
    for shop in shopping_data["shops"]:
        shops_dict[shop["name"]] = Shop(shop)
    customer_count = 0
    for customer in customers_dict.values():
        lowest_price, cheapest_shop = (
            customer.shop_selection(shops_dict, fuel_price)
        )
        if lowest_price > customer.money:
            customer.not_enough_money()
        else:
            customer.shopping_trip(cheapest_shop, lowest_price)
        customer_count += 1
        if customer_count < len(customers_dict):
            print()
