from decimal import Decimal
from app.customer import Customer
from app.shop import Shop


def shopping_in_the_store(customer: Customer, shop: Shop) -> None:
    print("Date: 04/01/2021 12:33:41")
    print(f"Thanks, {customer.name}, for your purchase!")
    keys_only = list(customer.product_cart.keys())
    milk_cost = Decimal(str(customer.product_cart["milk"]
                            * shop.products["milk"]))
    bread_cost = Decimal(str(int(customer.product_cart["bread"]
                                 * shop.products["bread"])))
    butter_cost = Decimal(str(customer.product_cart["butter"]
                              * shop.products["butter"]))
    print("You have bought:")
    print(f"{customer.product_cart["milk"]} {keys_only[0]}s"
          f" for {milk_cost} dollars")
    print(f"{customer.product_cart["bread"]} {keys_only[1]}s"
          f" for {bread_cost} dollars")
    print(f"{customer.product_cart["butter"]} {keys_only[2]}s"
          f" for {butter_cost} dollars")
    print(f"Total cost is {milk_cost + bread_cost + butter_cost} dollars\n"
          f"See you again!")
    print("")
