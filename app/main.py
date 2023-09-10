from app.trip_processor import TripProcessor


def shop_trip() -> None:
    container = TripProcessor()
    container.process_users()
