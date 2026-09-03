class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.location = location
        self.products = products
        self.name = name

    def print_receipt(self, customer_name: str, product_cart: dict) -> str:
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product_name, amount in product_cart.items():
            price = self.products[product_name]
            cost = price * amount
            if cost == int(cost):
                cost = int(cost)
            total_cost += cost
            if total_cost == int(total_cost):
                total_cost = int(total_cost)
            print(f"{amount} {product_name}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
