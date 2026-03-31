import datetime

from app.customer import (
    create_customer,
    count_total_fuel_price,
    counting_shopping_price,
)
from app.loading_file import open_json_file
from app.shop import create_shop


def shop_trip() -> None:
    data = open_json_file()
    customers = create_customer(data)
    shops = create_shop(data)

    for customer in customers:
        total = {}

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = (
                count_total_fuel_price(customer, shop, data)
                + counting_shopping_price(customer, shop)
            )
            total[shop] = trip_cost
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{trip_cost:.2f}"
            )

        cheapest_shop = min(total, key=total.get)
        cheapest_cost = total[cheapest_shop]

        if customer.money < cheapest_cost:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")
        print()

        customer.location = cheapest_shop.location

        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, amount in customer.product_cart.items():
            product_price = amount * cheapest_shop.products[product]

            if product_price.is_integer():
                product_price = int(product_price)

            print(f"{amount} {product}s for {product_price:.2f} dollars")

        shopping_cost = counting_shopping_price(customer, cheapest_shop)
        print(f"Total cost is {shopping_cost:.2f} dollars")
        print("See you again!")
        print()

        customer.money -= cheapest_cost
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()
