class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def make_recipe(self, customer_products: dict) -> None:
        total_price = 0
        for product_name, product_count in customer_products.items():
            for product, price in self.products.items():
                if product == product_name:
                    cost_product = price * product_count
                    total_price += cost_product
                    if cost_product % 1 == 0:
                        print(
                            f"{product_count} {product_name}s "
                            f"for {int(cost_product)} dollars"
                        )
                    else:
                        print(
                            f"{product_count} {product_name}s "
                            f"for {cost_product} dollars"
                        )
        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")
