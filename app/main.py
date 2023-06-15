from app.container import TripProcessor


def shop_trip() -> None:
    container = TripProcessor()
    container.process_users()
