import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def bill(self, customer_name: str, customer_product_car: dict) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        total_cost = 0
        print("You have bought: ")

        for product, quantity in customer_product_car.items():
            total_product = self.products[product] * quantity
            valid_name = product + "s" if quantity > 1 else product
            print(f"{quantity} {valid_name} for {total_product} dollars")
            total_cost += total_product
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
