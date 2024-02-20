from app.get_info import info_from_file
from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: Customer) -> None:
        current_time = "04/01/2021 12:33:41"
        print(f"\nDate: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            product_cost = quantity * self.products[product]
            total_cost += product_cost
            if int(product_cost) == product_cost:
                product_cost = int(product_cost)
            print(f"{quantity} {product}s for {product_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")


shops = {}

for shop in info_from_file["shops"]:
    shops[shop["name"]] = Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    )
