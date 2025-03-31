class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def products_cost(self, products: dict) -> float:
        counter = 0
        for product, amount in products.items():
            counter += amount * self.products.get(product, 0)
        return counter

    def buy(self, products: dict) -> None:
        print("You have bought:")

        total_cost = 0
        for product, amount in products.items():
            cost = round(amount * self.products.get(product, 0), 2)
            total_cost += cost
            cost_formatted = f"{cost}".rstrip("0").rstrip(".")
            print(f"{amount} {product}s for {cost_formatted} dollars")

        total_cost_formatted = f"{total_cost}".rstrip("0").rstrip(".")
        print(f"Total cost is {total_cost_formatted} dollars")
        print("See you again!\n")
