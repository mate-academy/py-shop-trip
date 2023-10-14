from app.customer import convert_file
import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict


def create_shop_list() -> list:
    markets = []
    for shop in convert_file()["shops"]:
        market = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        markets.append(market)
    return markets
