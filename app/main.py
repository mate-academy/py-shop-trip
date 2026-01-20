import json
from pathlib import Path

from app.trips.trip import Trip
from app.customers.customer import Customer
from app.shops.shop import Shop


base_dir = Path(__file__).resolve().parent
file_name = "config.json"


def get_data_from_file() -> tuple:
    with open(base_dir / file_name, "r") as file:
        file_data = json.load(file)
        return (
            file_data["FUEL_PRICE"],
            file_data["customers"],
            file_data["shops"]
        )


def shop_trip() -> None:

    fuel_price, customers, shops = get_data_from_file()
    customers = [Customer(**customer_info) for customer_info in customers]
    shops = [Shop(**shop_info) for shop_info in shops]

    for customer in customers:
        Trip(fuel_price, customer, shops).print_trip_log()
