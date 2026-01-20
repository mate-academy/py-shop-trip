from app.functions_to_interact_with_config import (
    get_file_config, get_file_dict
)


class Shop:
    def __init__(self, my_dict: dict) -> None:

        for key in my_dict:
            setattr(self, key, my_dict[key])


shops_config = get_file_config("shops")
shops_dict = get_file_dict(shops_config, "shops")
shops = {}

for name, info in shops_dict.items():
    shops[name] = Shop(info)
