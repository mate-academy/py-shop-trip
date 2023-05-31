from app.trip import Trip
import json


def shop_trip() -> None:
    trip = Trip()
    with open("app/config.json", "r") as config:
        initial_data = json.load(config)
    trip.get_trip_data(initial_data)
    trip.go_trip()


shop_trip()
