from app.customer_trip import Trip


def shop_trip() -> None:
    Trip(Trip.open_file("app/config.json")).customer_trip()
