import json
from pathlib import Path

from app.customer import Customers
from app.shops import Shops


def shop_trip() -> None:
    path_ = Path(__file__).parent.parent
    path_new = path_.joinpath("app").joinpath("config.json")
    with open(path_new, "r") as data_file:
        config_file = json.load(data_file)
        fuel_price = config_file["FUEL_PRICE"]

        for shop in config_file["shops"]:
            market = Shops(shop)
        for customer in config_file["customers"]:
            person = Customers(customer)

            Customers.choice_of_options(person, market, fuel_price)


if __name__ == "__main__":
    shop_trip()
