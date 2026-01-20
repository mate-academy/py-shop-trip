import json

from app.customer import Customer
from app.shop import Shop
from app.show_information import show_trip_info


def shop_trip() -> None:
    with open("app/config.json", "rb") as data_file:
        data = json.load(data_file)

    fuel_price = data["FUEL_PRICE"]

    customers_instances = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        )
        for customer in data["customers"]
    ]
    shops_instances = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]

    for customer in customers_instances:
        customer.calculate_total_expenses(shops_instances, fuel_price)
        customer.choose_shop_with_minimal_expenses()
        for shop, value in customer.best_shop.items():
            show_trip_info(customer, value)
