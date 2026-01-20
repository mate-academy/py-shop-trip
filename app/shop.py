import datetime

from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int, int],
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def serve_customer(self, customer: Customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, amount in customer.product_cart.items():
            product_name = product + "s" if amount > 1 else product
            cost = amount * self.products.get(product, 0)
            total_cost += cost

            if isinstance(cost, float) and cost.is_integer():
                cost = int(cost)
            print(f"{amount} {product_name} for {cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
