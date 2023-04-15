from app.car import Car
from app.convert_from_json import customers
from app.customer import Customer


def shop_trip() -> None:
    for client in customers:
        Customer(
            client["name"],
            client["product_cart"],
            client["location"],
            client["money"],
            Car(client["car"]["brand"],
                client["car"]["fuel_consumption"])).customers_money()
