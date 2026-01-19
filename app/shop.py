class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def price_products(
            self,
            quantity_milk: int,
            quantity_bread: int,
            quantity_butter: int
    ) -> float:
        return (self.products["milk"] * quantity_milk
                + self.products["bread"] * quantity_bread
                + self.products["butter"] * quantity_butter)
