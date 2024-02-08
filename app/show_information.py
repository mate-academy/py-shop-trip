import datetime

from app.customer import Customer


def show_trip_info(
        customer: Customer,
        total_price: float
) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    for shop, value in customer.total_expenses_for_every_shop.items():
        print(f"{customer.name}'s trip to the {shop.name} costs {value}")

    for shop, value in customer.best_shop.items():
        if customer.money > value:
            curr_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"{customer.name} rides to {shop.name}\n\n"
                  f"Date: {curr_date}\n"
                  f"Thanks, {customer.name}, for your purchase!\n"
                  f"You have bought:")
            for product, price in shop.products.items():
                product_price = customer.product_cart[product] * price
                if product_price == 3.0:
                    product_price = 3
                print(f"{customer.product_cart[product]} {product}s for "
                      f"{product_price} dollars")
            products_cost = customer.cost_of_all_products_to_buy(shop.products)
            print(f"Total cost is {products_cost} dollars\n"
                  "See you again!\n\n"
                  f"{customer.name} rides home\n"
                  f"{customer.name} now has "
                  f"{customer.money - total_price} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
