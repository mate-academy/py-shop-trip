import datetime

from app.instances.customer import Customer
from app.instances.shop import Shop


def print_shop_receipt(customer: Customer, shop: Shop) -> None:
    current_date = datetime.datetime.now()

    print(
        f"Date: {current_date.strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"Thanks, {customer.name}, for you purchase!\n"
        f"You have bought: "
    )

    total_cost = 0

    for product_name, quantity in customer.product_cart.items():
        if product_name in shop.products:
            products_cost = shop.products.get(product_name) * quantity
            total_cost += products_cost
            print(f"{quantity} {product_name}s for {products_cost} dollars")

    print(
        f"Total cost is {total_cost} dollars\n"
        "See you again!\n"
    )
