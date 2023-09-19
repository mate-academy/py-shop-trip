import os

import datetime

from app.bild_classes import (
    create_shops,
    create_customers,
    create_day_mark)

from app.controller import CustomersTrips


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")

    customers = create_customers(config_path)
    shops = create_shops(config_path)
    day = create_day_mark(config_path, formatted_datetime)

    trips = CustomersTrips(
        customers=customers,
        shops=shops,
        day=day
    )

    trips.print_trip_message()

