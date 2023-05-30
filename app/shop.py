import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict


def create_shop_from_file(data) -> list[Shop]:
    shops_data = data["shops"]

    shops = [Shop(
        name=shop['name'],
        location=shop['location'],
        products=shop['products']
    ) for shop in shops_data]
    return shops
