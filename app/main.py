import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data.get("FUEL_PRICE")
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"],
        )
        for customer in data["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]

    for person in customers:
        person.trip(shops, fuel_price)


shop_trip()
