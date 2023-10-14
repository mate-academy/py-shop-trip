from app.customer import file_content
import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict


markets = []

for shop in file_content["shops"]:
    market = Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    )
    markets.append(market)
