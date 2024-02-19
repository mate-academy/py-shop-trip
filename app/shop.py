class Shop:
    def __init__(self, name: str, location: list[int],
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def distance_to_shop(self, user_location: list[int]) -> float:
        return ((self.location[0] - user_location[0]) ** 2
                + (self.location[1] - user_location[1]) ** 2) ** 0.5

    def prices_of_products(self, product_cart: dict) -> float:
        products_cost = 0
        for product, value in product_cart.items():
            products_cost += value * self.products.get(product)
        return products_cost

    def possibility_of_purchase(self, name: str, product_cart: dict) -> None:
        print("\nDate: 04/01/2021 12:33:41")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        products_cost = 0
        for product, value in product_cart.items():
            product_cost = value * self.products.get(product)
            print(f"{value} {product}s for"
                  f" {str(product_cost).rstrip("0").rstrip(".")} dollars")
            products_cost += product_cost
        print(f"Total cost is {products_cost} dollars")
        print("See you again!\n")
