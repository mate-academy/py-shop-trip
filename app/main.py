"""Module for running the shop trip simulation."""
import json

from app.shop_trip import ShopTrip


def shop_trip() -> None:
    """
    Run the shop trip simulation based on the config file.
    """
    file_json_path = "app/config.json"
    with open(file_json_path, "r") as data:
        ShopTrip(data=json.load(data)).run_event()


if __name__ == "__main__":
    shop_trip()