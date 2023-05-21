import datetime
from math import dist
from app.shop import Shop
from app.customer import Customer


def calculate_cost_of_the_trip(
    customer: Customer, fuel_price: float, shop: Shop
) -> float:
    distance = dist(customer.location, shop.location)
    cost_1 = round(
        (customer.car.fuel_consumption / 100) * (distance * 2) *
        fuel_price, 2
    )
    cost_2 = 0
    for product, quantity in customer.wanted_products.items():
        cost_2 += shop.provided_products.get(product, 0) * quantity
    return cost_1 + cost_2


def choose_shop(customer: Customer,
                shops: list[Shop],
                fuel_price: float) -> int:
    min_trip_cost = float("inf")
    chosen_shop_index = -1

    for i, shop in enumerate(shops):
        trip_cost = calculate_cost_of_the_trip(
            customer, fuel_price, shop
        )
        print(f"{customer.name}'s trip "
              f"to {shop.name} costs {trip_cost}")

        if trip_cost < min_trip_cost:
            min_trip_cost = trip_cost
            chosen_shop_index = i

    return chosen_shop_index


def can_afford_trip(customer: Customer,
                    shops: list[Shop],
                    fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop_index = choose_shop(
        customer, shops, fuel_price
    )

    if cheapest_shop_index != -1:
        trip_cost = calculate_cost_of_the_trip(
            customer, fuel_price, shops[cheapest_shop_index]
        )
        if trip_cost < customer.money:
            go_to_shop(customer, shops[cheapest_shop_index])
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
    else:
        print(f"No shop available for {customer.name}")


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


def go_to_shop(
    customer: Customer,
    shop: Shop,
) -> None:
    trip_price = customer.trip_cost
    customer.money -= trip_price
    print(f"{customer.name} rides to {shop.name}\n")
    shop_print(shop, customer)
    print(f"\n{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars\n")
