class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def what_you_want_to_buy(self, wish_dict: dict) -> float:

        total = 0
        for product_name, quantity in wish_dict.items():
            total += quantity * self.products.get(product_name, 0)

        return total
