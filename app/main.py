import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    shops = config.get("shops")
    customers_data = config.get("customers")
    fuel_price = config.get("FUEL_PRICE")

    customers_instances = [Customer(
        name=customer_data["name"],
        products=customer_data["product_cart"],
        location=customer_data["location"],
        money=customer_data["money"],
        car=Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"]
        )
    ) for customer_data in customers_data]

    shops_instances = [Shop(
        name=shop_data.get("name"),
        location=shop_data.get("location"),
        products=shop_data.get("products")
    ) for shop_data in shops]

    for customer_instance in customers_instances:
        selected_shop = customer_instance.define_shop(
            shops=shops_instances,
            fuel_price=fuel_price
        )
        if selected_shop:
            customer_instance.make_purchase(selected_shop=selected_shop)
            customer_instance.ride_home()
