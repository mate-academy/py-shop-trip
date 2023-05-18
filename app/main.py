import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data.get("FUEL_PRICE")
    customers = []
    for customer in data["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"],
        ))

    shops = []
    for shop in data["shops"]:
        shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))

    for person in customers:
        person.find_min_cost_shop(shops, fuel_price)
        person.trip(shops, fuel_price)


shop_trip()
