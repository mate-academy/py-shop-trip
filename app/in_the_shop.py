from decimal import Decimal
from app.customer import Customer
from app.shop import Shop


def shopping_in_the_store(customer: Customer, shop: Shop) -> None:
    print("Date: 04/01/2021 12:33:41")
    print(f"Thanks, {customer.name}, for your purchase!")
    amount_of_milk = customer.product_cart["milk"]
    amount_of_bread = customer.product_cart["bread"]
    amount_of_butter = customer.product_cart["butter"]
    milk_cost = Decimal(str(customer.product_cart["milk"]
                            * shop.products["milk"]))
    bread_cost = Decimal(str(int(customer.product_cart["bread"]
                                 * shop.products["bread"])))
    butter_cost = Decimal(str(customer.product_cart["butter"]
                              * shop.products["butter"]))
    print("You have bought:")
    print(f"{amount_of_milk} milks for {milk_cost} dollars")
    print(f"{amount_of_bread} breads for {bread_cost} dollars")
    print(f"{amount_of_butter} butters for {butter_cost}"
          f" dollars")
    print(f"Total cost is {milk_cost + bread_cost + butter_cost} dollars")
    print("See you again!")
    print("")
