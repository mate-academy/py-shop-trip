import dataclasses
from app.customer import data


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict


shops_data = data["shops"]

shops = [Shop(
    name=shop['name'],
    location=shop['location'],
    products=shop['products']
) for shop in shops_data]

