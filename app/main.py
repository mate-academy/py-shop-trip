import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)

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

    shop_instances = [Shop(**shop_data) for shop_data in shops]

    for customer_instances in customers_instances:
        chosen_shop = customer_instances.define_shop(
            shops=shop_instances,
            fuel_price=fuel_price
        )
        if chosen_shop:
            customer_instances.make_purchase(chosen_shop=chosen_shop)
            customer_instances.ride_home()
