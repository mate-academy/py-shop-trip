from app.best_shop_finder import get_best_shop
from app.json_reader import read_json


def shop_trip() -> None:
    info = read_json()
    get_best_shop(info)
