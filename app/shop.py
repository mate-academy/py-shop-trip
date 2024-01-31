import datetime

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_cart(self, product_cart: dict) -> float:
        return sum(self.products[product] * product_cart[product]
                   for product in product_cart.keys())

    def purchase(self, customer: Customer) -> None:
        current_date = datetime.datetime.now()
        print(f'Date: {current_date.strftime("%d/%m/%Y %H:%M:%S")}')
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")  # noqa
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            cost = quantity * self.products[product]
            if cost - int(cost) == 0:
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
