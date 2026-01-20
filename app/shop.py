class Shop:
    def __init__(
            self,
            name: str,
            shop_location: list,
            products: dict
    ) -> None:
        self.shop_name = name
        self.shop_location = shop_location
        self.products = products

    def calculate_product_cost(self, product: dict) -> float:
        all_price = 0
        for item, quantity in product.items():
            if item in self.products:
                product_price = self.products[item]
                all_price += product_price * quantity
        return all_price
