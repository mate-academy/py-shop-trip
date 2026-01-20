from app.open_file_config import OpenFileConfig


def shop_trip() -> None:
    opened_file_config = OpenFileConfig.open_file_config(
        "app/config.json"
    )
    customer_instances, shop_instances = OpenFileConfig.creation_instances(
        opened_file_config
    )
    for customer in customer_instances:
        customer.choose_shop_and_go_to_trip(
            shop_instances=shop_instances
        )
