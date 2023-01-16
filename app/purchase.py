from app.customer import Customer
from app.shop import Shop
import datetime


def receipt(customer: Customer, shop: Shop) -> None:
    current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {current_date}")
    print(f"Thanks, {customer.name}, for you purchase!")
    print("You have bought: ")
    product_cost = 0
    for product, quantity in customer.product_cart.items():
        product_cost += shop.products[product] * quantity
        print(f"{quantity} {product}s for "
              f"{shop.products[product] * quantity} dollars")
    print(f"Total cost is {product_cost} dollars")
    print("See you again!\n")
    print(f"{customer.name} rides home")
