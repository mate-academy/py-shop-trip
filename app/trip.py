import math
from app.customer import Customer
from app.shop import Shop, shops
from app.get_info import info_from_file


def calculate_cost_of_trip(
        customer: Customer,
        shop: Shop
) -> None:
    distance = math.sqrt(
        (customer.location[0] - shop.location[0]) ** 2
        + (customer.location[1] - shop.location[1]) ** 2
    )
    fuel_cost = round(
        2
        * distance
        * customer.car.fuel_consumption
        / 100
        * info_from_file["FUEL_PRICE"], 2
    )
    cart_cost = 0
    for product_name, product_cost in customer.product_cart.items():
        cart_cost += product_cost * shop.products[product_name]
    return fuel_cost + cart_cost


def find_best_trip(customer: Customer) -> Shop:
    result = {
        shop: calculate_cost_of_trip(customer, shop) for shop in shops.values()
    }
    min_cost = min(result.values())
    for shop, cost in result.items():
        if cost == min_cost:
            return shop


def trip_by_car(customer: Customer) -> None:
    for shop in shops.values():
        trip_cost = calculate_cost_of_trip(customer, shop)
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {trip_cost}")

    shop = find_best_trip(customer)
    if customer.money >= calculate_cost_of_trip(customer, shop):
        print(f"{customer.name} rides to {shop.name}")
        shop.print_receipt(customer)
        print(f"\n{customer.name} rides home")
        print(
            f"{customer.name} now has "
            f"{customer.money - calculate_cost_of_trip(customer, shop)}"
            f" dollars\n"
        )
    else:
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
