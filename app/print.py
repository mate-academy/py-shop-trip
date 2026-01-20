from app.car import Car
from app.customer import Customer
from app.shop import Shop
import datetime


def get_shopping_options(
        car: Car,
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> None:
    print(f"{customer.name}'s trip to the {shop.name} costs "
          f"{car.get_total_trip_cost(customer, shop, fuel_price)}")


def get_receipt(
        customer: Customer,
        shop: Shop
) -> None:
    print(f"{customer.name} rides to {shop.name}")

    current_date = datetime.datetime.now()
    print(f"\nDate: {current_date.strftime('%d/%m/%Y %H:%M:%S')}\n"
          f"Thanks, {customer.name}, for you purchase!\n"
          f"You have bought: ")

    for product in customer.product_cart:
        number = customer.product_cart[product]
        price = number * shop.products[product]
        print(f"{number} {product}s for {price} dollars")
    print(f"Total cost is "
          f"{shop.get_shopping_cost(customer)} dollars\n"
          f"See you again!\n")


def get_home(
        car: Car,
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> None:
    total_cost = car.get_total_trip_cost(
        customer, shop, fuel_price
    )
    rest_on_balance = customer.money - total_cost
    print(f"{customer.name} rides home\n"
          f"{customer.name} now has {rest_on_balance} dollars\n")


def not_enough_money(customer: Customer) -> None:
    print(f"{customer.name} doesn't have enough money "
          f"to make purchase in any shop")
