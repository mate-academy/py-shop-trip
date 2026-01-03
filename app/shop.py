import json


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def get_list_of_shops(cls) -> list:
        with open("app/config.json", "r") as file:
            data = json.load(file)

        shops = get_shop_list(data)
        return shops


def get_shop_list(data: dict) -> list[Shop]:
    shops_list = data.get("shops")
    return [
        Shop(**shop)
        for shop in shops_list
    ]
