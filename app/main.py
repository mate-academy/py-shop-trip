import json
from app.shop import Shop
from app.customer import Customer
from app.best_shop import locate_and_buy_in_the_best_shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(
        c["name"],
        c["product_cart"],
        c["location"],
        c["money"],
        c["car"]["fuel_consumption"]) for c in data["customers"]]
    shops = [Shop(
        s["name"],
        s["location"],
        s["products"]) for s in data["shops"]]

    locate_and_buy_in_the_best_shop(customers, shops, fuel_price)
