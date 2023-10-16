from app.customer import convert_file
import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict


def create_shops() -> list:
    markets = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in convert_file()["shops"]]

    return markets
