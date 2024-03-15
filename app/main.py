from app.file import OpenFile


def shop_trip() -> None:
    opened_file_config = OpenFile.open_file_config(
        "app/config.json"
    )
    customer_instances, shop_instances = OpenFile.creation_instances(
        opened_file_config
    )
    for customer in customer_instances:
        customer.choose_shop_and_go_to_trip(
            shop_instances
        )
