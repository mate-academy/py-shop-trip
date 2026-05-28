import json

from app.core import Core


def shop_trip() -> None:
    with open("app/config.json" , "r") as json_file:
        data = json.load(json_file)

    Core(data).run()
