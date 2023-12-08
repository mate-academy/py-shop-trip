from datetime import datetime


class Customer:
    def __init__(self,
                 customer_name: str,
                 products_cart: dict,
                 customer_location: list,
                 money: int,
                 car: dict
                 ) -> None:
        self.customer_name = customer_name
        self.products_cart = products_cart
        self.customer_location = customer_location
        self.money = money
        self.car = car


class Shop:
    def __init__(self,
                 name: str,
                 shop_location: list,
                 products: dict
                 ) -> None:
        self.name = name
        self.shop_location = shop_location
        self.products = products


def shopping_time(customer: Customer, shop: Shop) -> None:
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Data: {current_time}")
    print(f"Thanks, {customer.customer_name}, for your purchase!")
    print(f"You have bought: ")
    total_cost = 0
    for product, quantity in customer.products_cart.items():
        if product in shop.products:
            cost_product = shop.products[product] * quantity

            print(f"{quantity} {product}(s) for a total cost of ${cost_product}")

        total_cost += (int(cost_product * quantity)
        if cost_product * quantity == int(cost_product * quantity)
        else cost_product * quantity)

    print(f"Total cost is {total_cost} dollars. \n See you again!")


customer = Customer("John Doe", {"milk": 2, "bread": 3, "butter": 1}, [10, -5], 100, {})
shop = Shop("Outskirts Shop", [10, -5], {"milk": 3, "bread": 1, "butter": 2.5})

shopping_time(customer, shop)

