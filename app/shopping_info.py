from datetime import datetime
from app.customer import Customer


def shopping_info(
        customer: Customer,
        cheapest_shop: list
) -> None:
    print(f"{customer.name} rides to {cheapest_shop[0].name}\n")
    date_time = datetime.now()
    print(f"Date: {date_time.strftime('%m/%d/%Y %H:%M:%S')}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    for product, value in customer.product_cart.items():
        shopping = cheapest_shop[0].products[product] * value
        print(f"{value} {product}s for {shopping} dollars")
    print(f"Total cost is {cheapest_shop[2]} dollars")
    print("See you again!\n")
    print(f"{customer.name} rides home")
    print(f"{customer.name} now has "
          f"{customer.money - cheapest_shop[1]} dollars\n")
