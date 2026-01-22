import json

from app.shop_trip_moduls.custom_functions import (
    create_data_customers,
    create_data_shops,
    play_shop_trip
)


def shop_trip() -> None:
    with open("app/config.json", "r") as story:
        data = json.load(story)
        shops = create_data_shops(data)
        customers = create_data_customers(data)
        play_shop_trip(shops, customers)
