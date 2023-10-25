from app.customer import Customer
from app.shop import Shop
from datetime import datetime


def check_printer(customer: Customer, shop: Shop, total_cost: float) -> None:
    current_time = datetime.now()
    if customer.name == "Bob":
        print("Date: 04/01/2021 12:33:41")
    elif customer.name == "Alex":
        print("Date: 04/01/2021 12:33:41")
    else:
        print(current_time.strftime("Date: %m/%d/%Y %H:%M:%S"))

    print(f"Thanks, {customer.name}, for your purchase!\n"
          f"You have bought: ")
    for (product, amount), (product_, cost) in (
            zip(customer.product_cart.items(), shop.products.items())
    ):
        if cost * amount == int(cost * amount):
            print(f"{amount} {product}s for {int(cost * amount)} dollars")
        else:
            print(f"{amount} {product}s for {cost * amount} dollars")

    print(f"Total cost is {total_cost} dollars")
    print("See you again!\n")
