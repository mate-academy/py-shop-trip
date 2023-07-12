import json
import os

from models.customer import Customer
from models.shop import Shop


def shop_trip() -> None:
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "config.json")
    with open(file_path, "r") as file:
        data = json.load(file)
        fuel_price = data.get("FUEL_PRICE", 1)
        customers = [Customer(**customer) for customer in data["customers"]]
        shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        data_costs = customer.cost_calculation(shops, fuel_price)
        customer.chose_and_visit_store(data_costs)


if __name__ == "__main__":
    shop_trip()
