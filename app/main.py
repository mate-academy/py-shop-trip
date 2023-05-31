from __future__ import annotations
import json
from app.trip import Trip


def shop_trip() -> None:
    trip = Trip()
    with open(r"app/config.json", "r") as config:
        initial_data = json.load(config)
    trip.get_trip_data(initial_data)
    trip.go_trip()


shop_trip()
