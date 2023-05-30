import json

from app.shop_trip_moduls.custom_functions import (
    create_data_customers,
    create_data_shops,
    play_shop_trip
)


def shop_trip() -> None:
    with open("config.json") as story:
        data = json.load(story)
        list_data_shops = create_data_shops(data)
        list_data_customers = create_data_customers(data)
        play_shop_trip(list_data_shops, list_data_customers)

# shop_trip()