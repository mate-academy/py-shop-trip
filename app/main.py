import json
from pathlib import Path

from app.instances.create_instances import transform_json_to_instances
from app.trip_details.shop_receipt import print_shop_receipt
from app.trip_details.visit_shop import (
    calculate_trips_costs_to_shops,
    check_if_can_ride_to_shop,
    ride_home,
    ride_to_shop)


def shop_trip() -> None:
    path_to_file = Path(__file__).parent.joinpath("config.json")
    with open(path_to_file) as file:
        raw_data = json.load(file)

    data = transform_json_to_instances(raw_data)

    for customer in data["customers"]:
        trip_cost = calculate_trips_costs_to_shops(
            data["FUEL_PRICE"],
            customer,
            data["shops"]
        )

        check_if_can_ride_to_shop(customer, trip_cost)

        if customer.has_enough_money:
            ride_to_shop(customer, customer.chosen_shop)
            print_shop_receipt(customer, customer.chosen_shop)
            ride_home(customer)


if __name__ == "__main__":
    shop_trip()
