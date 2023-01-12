from app.info import get_information


class Shop:

    def __init__(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            setattr(self, key, value)


def create_class_instance_shops_list() -> list:
    shops_list = get_information()["shops"]
    shops_class_list = []
    for shop in shops_list:
        shops_class_list.append(Shop(shop))
    return shops_class_list
