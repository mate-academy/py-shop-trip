from app.config_loader import load_config
from app.product import Product


config = load_config()
shops = config["shops"]


class Shop:
    def __init__(self, shop_params: dict) -> None:
        self.name: str = shop_params["name"]
        self.location: list[int] = shop_params["location"]
        self.products: list[Product] = [
            Product(product, price)
            for product, price in shop_params["products"].items()
        ]
