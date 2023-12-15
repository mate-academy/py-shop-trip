class Shop:

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shop_total_coast(self, product_cart: dict) -> float:
        coast = 0
        for product in product_cart:
            coast += product_cart.get(product) * self.products.get(product)
        return coast

    def print_check(self, customer_name: str, product_cart: dict) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product in product_cart:
            cost = product_cart.get(product) * self.products.get(product)
            cost = int(cost) if cost == int(cost) else cost
            print(f"{product_cart.get(product)} {product}s for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
