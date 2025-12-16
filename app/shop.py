class Shop:
    def __init__(self, shop_dict: dict) -> None:
        self.name = shop_dict["name"]
        self.coords = shop_dict["location"]
        self.products = shop_dict["products"]

    def purchase_receipt(self, product_cart: dict) -> dict:
        receipt = {}
        for product in product_cart.keys():
            receipt[product] = product_cart[product] * self.products[product]
        return receipt
