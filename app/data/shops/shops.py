from app.data.location import Location


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = Location(*location)
        self.products_price = products

    def price_shop(self, count_products: dict) -> float:
        for product in self.products_price:
            self.products_price[product] = count_products[product]
        return sum()
