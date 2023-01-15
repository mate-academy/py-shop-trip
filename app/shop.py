from app.location import Location


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = Location(shop["location"])
        self.products = shop["products"]

    def check_if_has_products(self, products_to_buy: dict) -> bool:
        for product in products_to_buy:
            if product not in self.products:
                return False
        return True

    def price_of_products(self, products_to_buy: dict) -> int | float:
        total_price = 0
        for product, quantity in products_to_buy.items():
            total_price += self.products[product] * quantity
        return total_price
