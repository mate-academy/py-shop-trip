from app.point import Point


class Shop:
    def __init__(self, name: str, location: Point, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def price_of_products_set(self, products_list: dict) -> int | float:
        return sum(
            self.products[key] * products_list[key] for key in products_list.keys()
        )
