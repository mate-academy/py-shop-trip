import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as f:
        items = json.load(f)
        fuel_price = items["FUEL_PRICE"]

        for shop in items["shops"]:
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        for customer in items["customers"]:
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"],
                fuel_price
            )


if __name__ == "__main__":
    shop_trip()
