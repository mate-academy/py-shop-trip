class Shop:

    def __init__(self, name: str, location: list[int], products: dict):
        self.name = name
        self.location = location
        self.products = products

    def print_purchase(self, customer):
        print("\nDate: 11/03/2020 13:15:34")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, value in customer.products_card.items():
            print(f"{value} {product}s for {self.products[product] * value} dollars")
        print(f"Total cost is {customer.calc_coast_for_all_in_product_cart(self)} dollars")
        print("See you again!\n")
