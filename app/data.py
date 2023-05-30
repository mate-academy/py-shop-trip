import json
from typing import Union
from app.customer import create_customer_from_file
from app.shop import create_shop_from_file


def parse_config(file_path: str) -> Union[tuple]:
    with open(file_path, "r") as file:
        data = json.load(file)

    return create_customer_from_file(data),\
        create_shop_from_file(data), data["FUEL_PRICE"]
