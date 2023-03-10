import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_purchase_receipt(self, customer: type(object)) -> float:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        total_cost = 0
        for product, amount in customer.product_cart.items():
            product_price = amount * self.products[product]
            print(f"{amount} {product}s for {product_price} dollars")
            total_cost += product_price

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        return total_cost
