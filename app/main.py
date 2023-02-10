import json
from pathlib import Path

from app.customer import Customer, Shop


def shop_trip() -> None:
    # read data from the file
    path_ = Path(__file__).parent.parent
    path_new = path_.joinpath("app").joinpath("config.json")
    with open(path_new, "r") as data_file:
        config_file = json.load(data_file)
        fuel_price = config_file["FUEL_PRICE"]

        # creating instances of the class
        for shop in config_file["shops"]:
            market = Shop(shop)
        for customer in config_file["customers"]:
            person = Customer(customer)
            # main function run
            person.trip_in_shop(market, fuel_price)


if __name__ == "__main__":
    shop_trip()
