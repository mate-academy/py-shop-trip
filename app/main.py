from app.customer_trip import Trip


def shop_trip() -> None:
    Trip.customer_trip(Trip.open_file("app/config.json"))
