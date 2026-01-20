import json
from app.car import Car
from app.point import Point
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        all_info = json.load(file)

    customers = []
    for customer in all_info["customers"]:
        new_customer = Customer(
            customer["name"],
            customer["product_cart"],
            Point(customer["location"][0], customer["location"][1]),
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"]),
        )
        customers.append(new_customer)

    shops = []
    for shop in all_info["shops"]:
        new_shop = Shop(
            shop["name"],
            Point(shop["location"][0], shop["location"][1]),
            shop["products"],
        )
        shops.append(new_shop)

    fuel_price = all_info["FUEL_PRICE"]
    for client in customers:
        client.check_shops(shops, fuel_price)


shop_trip()
