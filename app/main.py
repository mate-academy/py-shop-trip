from app.info_display import display_info
from app.json_reader import read_json


def shop_trip() -> None:
    info = read_json()
    display_info(info)
