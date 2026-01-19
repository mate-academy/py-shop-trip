class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self. location = location
        self.products = products

    def products_cost(self, client_products: dict) -> int:
        total = 0
        for product_name, amount in client_products.items():
            if product_name in self.products:
                total += self.products[product_name] * amount
            else:
                return -1
        return total

    def purchase_receipt(self,
                         client_name: str,
                         client_products: dict,
                         total_cost: float) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {client_name}, for your purchase!")
        print("You have bought:")
        for product_name, amount in client_products.items():
            value = round(self.products[product_name] * amount, 2)
            final_value = int(value) if isinstance(value, float) and value.is_integer() else value
            print(f"{amount} {product_name}s for"
                  f" {round(final_value, 2)} dollars")
        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!")
