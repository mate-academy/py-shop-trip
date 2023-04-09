from app.car import Car
from app.customers_config import Customer
from app.convert import customers_list


def shop_trip() -> None:
    for client in customers_list:
        Customer(
            client["name"],
            client["product_cart"],
            client["location"],
            client["money"],
            Car(client["car"]["brand"],
                client["car"]["fuel_consumption"])).customers_money()
