from app.trip import Trip


def shop_trip() -> None:
    trip = Trip()
    trip.get_trip_data("app/config.json")
    trip.go_trip()


shop_trip()
