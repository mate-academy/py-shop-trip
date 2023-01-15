import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    with open("app/config.json") as file_config:
        items = json.load(file_config)
        fuel_price = items["FUEL_PRICE"]

        for shop in items["shops"]:
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        for car in items["customers"]:
            Car(car["name"], car["car"], fuel_price)

        for customer in items["customers"]:
            customers.append(Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
            ))
    for customer in customers:
        customer.count_price_fuel_and_products(Shop.shops, Car.cars)


if __name__ == "__main__":
    shop_trip()
