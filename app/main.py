import os
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    app_folder_path = os.path.dirname(os.path.abspath(__file__))
    file_name = "config.json"
    config_json = os.path.join(app_folder_path, file_name)
    Shop.parse_data_from_json("shops", config_json)
    Customer.parse_data_from_json("customers", config_json)
    Car.parse_data_from_json("fuel", config_json)
    for person in Customer.customers:
        print(f"{person.name} has {person.money} dollars")
        person.calculate_costs_shopping_per_shop()
        person.choose_cheapest_shop()
        person.bill_shipping()
