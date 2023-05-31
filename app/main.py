from __future__ import annotations
from app.trip import Trip


def shop_trip() -> None:
    trip = Trip()
    trip.get_trip_data(
        r"config.json"
    )
    trip.go_trip()


if __name__ == "__main__":
    shop_trip()
