import datetime
from app.customer import Customer


class Receipt:
    def __init__(self, customer: Customer, shop: "Shop") -> None:
        self.customer = customer
        self.shop = shop
        self.total_cost = 0
        self.final_balance = 0

    def calculate_total_cost(self) -> int:
        money_available = self.customer.money
        self.final_balance = self.customer.money - self.total_cost

        for product, quantity in self.customer.product_cart.items():
            if product in self.shop.products:
                product_cost = self.shop.products[product] * quantity
                if product_cost <= money_available:
                    money_available -= product_cost
                    self.total_cost += product_cost

        return self.total_cost

    def print_receipt(self) -> None:
        print("You have bought:")
        for product, quantity in self.customer.product_cart.items():
            if product in self.shop.products:
                product_cost = self.shop.products[product] * quantity
                product_cost = (
                    int(product_cost) if product_cost % 1 == 0
                    else product_cost
                )
                print(f"{quantity} {product}s for {product_cost} dollars")

        print(f"Total cost is {self.total_cost} dollars")


class Shop:
    def __init__(self, name: str, location: list, products: dict,) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_to_buy(
            self, customer: Customer,
            total_cost: int | float
    ) -> None:
        receipt = Receipt(customer, self)
        receipt.calculate_total_cost()
        receipt.print_receipt()
        final_balance = customer.money - total_cost
        print("See you again!\n"
              f"\n{customer.name} rides home\n"
              f"{customer.name} now has {final_balance} dollars\n")

    @staticmethod
    def get_current_datetime() -> str:
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_datetime
