class Shop:
    shop_list = []

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.shop_list.append(self)

    @staticmethod
    def create_from_dict(shops: dict) -> None:
        for current_shop in shops:
            Shop(
                current_shop["name"],
                current_shop["location"],
                current_shop["products"]
            )

    def cost_of_all_products(self, product_cart: dict) -> int:
        cost = 0
        for product, amount in product_cart.items():
            cost += amount * self.products[product]
        return cost
