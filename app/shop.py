import datetime
from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost_customer(self, customer: Customer) -> float:
        products_cost = 0
        for key in customer.product_cart:
            products_cost += customer.product_cart[key] * self.products[key]
        return products_cost

    def shopping_process(self, customer: Customer) -> float:
        products_cost = 0
        print("Date: "
              + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for key in customer.product_cart:
            set_cost = 0
            set_cost = customer.product_cart[key] * self.products[key]
            if set_cost == 1 | 0:
                print(f"{customer.product_cart[key]} {key} " + "for "
                      + f"{str(set_cost).rstrip('0').rstrip('.')} dollars")
            else:
                print(f"{customer.product_cart[key]} {key}s " + "for "
                      + f"{str(set_cost).rstrip('0').rstrip('.')} dollars")
            products_cost += set_cost

        print(f"Total cost is {products_cost} dollars")
        print("See you again!" + "\n")
        return products_cost
