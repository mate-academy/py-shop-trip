class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = tuple(data["location"])
        self.products = data["products"]

    def total_products_cost(self, card_dict: dict) -> float:
        total = 0.0
        for name, qty in card_dict.items():
            price = self.products.get(name)
            if price is None:
                continue
            total += price * qty
        return total
