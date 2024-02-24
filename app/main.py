from app.open_file_config import OpenFileConfig
from app.trip import Trip


def shop_trip() -> None:
    customer_instances, shop_instances = OpenFileConfig.take_data_from_config(
        "app/config.json"
    )
    Trip.choose_shop_and_go_to_trip(
        customer_instances=customer_instances,
        shop_instances=shop_instances
    )
