import datetime

from app.shop import Shop
from app.customer import Customer
from app.trip.trip import calculate_cost_of_the_trip


def shop_print(shop: Shop, customer: Customer) -> None:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought: ")
    total_cost = 0
    for product, count in customer.wanted_products.items():
        total_cost += count * shop.provided_products.get(product, 0)
        print(
            f"{count} {product if count < 2 else product + 's'} "
            f"for {count * shop.provided_products.get(product, 0)} dollars"
        )
    print(f"Total cost is {round(total_cost, 2)} dollars")
    print("See you again!")


def go_to_shop(customer: Customer, shop: Shop, fuel_price: float) -> None:
    trip_price = calculate_cost_of_the_trip(customer, fuel_price, shop)
    customer.money -= trip_price
    print(f"{customer.name} rides to {shop.name}\n")
    shop_print(shop, customer)
    print(f"\n{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars\n")
