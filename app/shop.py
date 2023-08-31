import datetime
import typing

if typing.TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def serve_customer(self, customer: "Customer", money_spent: int) -> None:
        now = datetime.datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        total_price = 0
        for product_name in customer.product_cart.keys():
            quantity = customer.product_cart[product_name]
            price = self.products[product_name]
            position_cost = quantity * price
            total_price += position_cost
            print(f"{quantity} {product_name}s for {position_cost} dollars")
        print(f"Total cost is {total_price} dollars")
        print("See you again!")
        print("")
        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has {customer.money - money_spent} dollars"
        )
        print("")
