import json
from app.customer import Customer
from app.shop import Shop
from app.trip import trip


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

        customers = [Customer(**customer) for customer in config["customers"]]
        shops = [Shop(**shop) for shop in config["shops"]]
        fuel_price = config["FUEL_PRICE"]

        for customer in customers:
            trip(customer, shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
