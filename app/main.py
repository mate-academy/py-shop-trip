from app import application


def shop_trip() -> None:
    app = application.load_from_json("app/config.json")
    app.process_the_data()
