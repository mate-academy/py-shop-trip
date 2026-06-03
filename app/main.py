import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = []
    for shop in config["shops"]:
        shops.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        ))

    customers = []
    for customer in config["customers"]:
        car = Car(
            brand=customer["car"]["brand"],
            fuel_consumption=customer["car"]["fuel_consumption"],
        )
        customers.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=car,
        ))

    for customer in customers:
        customer.do_shopping(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
