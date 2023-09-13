import os
from app.utils.object_creator import create_shops
from app.utils.object_creator import create_customers
from app.utils.config_reader import config_reader
from app.utils.shopping_logic import go_shopping
from app.customer import Customer


def shop_trip() -> None:
    config_data = config_reader(
        current_dir=os.path.dirname(os.path.abspath(__file__)),
        filename="config.json"
    )
    customers: list = create_customers(config_data["customers"])
    shops: list = create_shops(config_data["shops"])
    Customer.fuel_price = config_data["FUEL_PRICE"]
    go_shopping(customers, shops)


if __name__ == "__main__":
    shop_trip()
