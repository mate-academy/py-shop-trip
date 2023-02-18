import math
from datetime import datetime

from app.customer import Customer
from app.shop import Shop


def find_cheapest_shop_and_trip(
        customer: Customer,
        shops: list,
        fuel_price: float,
) -> tuple | float:
    cheapest_trip = 0
    cheapest_total = 0

    for i in range(len(shops)):
        distance = math.dist(customer.location, shops[i].location) * 2
        trip_price = round(
            (customer.car.fuel_consumption * fuel_price / 100) * distance, 2
        )
        product_price = 0
        for name, quountity in customer.product_cart.items():
            product_price += (
                quountity * shops[i].products[name]
            )
        total_price = product_price + trip_price
        print(
            f"{customer.name}'s trip to the "
            f"{shops[i].name} costs {total_price}"
        )
        if cheapest_trip == 0 or cheapest_trip > trip_price and (
            cheapest_total == 0 or cheapest_total > total_price
        ):
            cheapest_trip = trip_price
            cheapest_shop = shops[i]
            cheapest_total = total_price

    return cheapest_shop, cheapest_trip, cheapest_total


def get_check(customer: Customer, cheapest_shop: Shop) -> None:
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total_cost = 0

    print(
        f"{today}\n"
        f"Thanks, {customer.name}, for you purchase!\n"
        f"You have bought:"
    )

    for name, price in cheapest_shop.products.items():
        total_cost += customer.product_cart[name] * price
        print(
            f"{customer.product_cart[name]} {name}s "
            f"for {customer.product_cart[name] * price} dollars"
        )
    print(
        f"Total cost is {total_cost} dollars\n"
        f"See you again!\n"
    )
