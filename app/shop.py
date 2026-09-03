class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict,
                 ) -> None:

        self.name = name
        self.location = location
        self.products = products

    def cart_cost(self, products_to_buy: dict) -> dict:
        cart_sum = 0
        products_prices = dict()

        for product_key, product_value in self.products.items():
            product_price = product_value * products_to_buy.get(product_key, 0)
            products_prices[product_key] = product_price
            cart_sum += product_price

        products_prices["cart_cost"] = round(cart_sum, 2)

        return products_prices
